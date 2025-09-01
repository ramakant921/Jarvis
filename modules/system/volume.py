from core.engine import speak
from sys import platform
import subprocess
try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except ImportError:
    pass

def adjust_linux_volume(level):
    subprocess.call(["amixer", "-D", "pulse", "sset", "Master", str(level*10)+"%"])

def adjust_windows_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    volume_levels = {
        "1": -33.0, "2": -23.5, "3": -17.7,
        "4": -13.5, "5": -10.3, "6": -7.61,
        "7": -5.3, "8": -3.3, "9": -1.5, "10": 0.0
    }
    volume.SetMasterVolumeLevel(volume_levels.get(level, 0.0), None)
    speak(f"Volume set to {level}.")

# Main Function
def adjust_volume(level):
    """Adjust the system volume based on the provided level (1-10)."""
    if platform == "linux" or platform == "linux2":
        adjust_linux_volume(int(level))
    elif platform == "win":
        adjust_windows_volume(int(level))