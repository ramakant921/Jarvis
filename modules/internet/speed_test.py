import speedtest
from core.engine import speak

def internet_speed_test():
    """Perform an internet speed test and report results."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1e6  # Convert to Mbps
        upload_speed = st.upload() / 1e6  # Convert to Mbps
        speak(f"Download Speed: {download_speed:.2f} Mbps. Upload Speed: {upload_speed:.2f} Mbps.")
    except Exception as e:
        print(f"Speed test error: {e}")
        speak("I couldn't perform the speed test. Please check your internet connection.")