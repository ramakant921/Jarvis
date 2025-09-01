from core.engine import speak

import pywhatkit
import pyautogui

def play_media(song):
    """Play media (YouTube song) based on the query."""
    if song:
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    else:
        speak("No song specified.")

def skip_or_rewind(command):
    # value = ''.join(filter(str.isdigit, command))
    if 'skip' in command or 'jump' in command:
        pyautogui.press('l')
    elif 'rewind' in command or 'go back' in command:
        pyautogui.press('j')

