from modules.internet.wikipedia import search_wikipedia
from modules.internet.speed_test import internet_speed_test
from modules.system.volume import adjust_volume
from modules.media.playback import play_media, skip_or_rewind
from modules.internet.open_website import open_website
from modules.system.brightness import change_brightness
# from modules.system.power_manager import power_manager
from modules.accessibility.keyboard import manage_keyboard
from plugin.interface import handle_device 
from core.engine import speak

import pyautogui

def handle_command(command):
    """Route commands to their respective handlers and provide feedback."""
    
    # Command: Wikipedia search
    if 'wikipedia' in command:
        query = command.replace("wikipedia", "").strip()
        search_wikipedia(query)

    elif 'open' in command:
        open_website(command)
    
    # Command: Play media (music/video)
    elif 'play' in command:
        song = command.replace("play", "").strip()
        if song:
            play_media(song)
    
    # Command: Adjust volume
    elif 'volume' in command:
        level = ''.join(filter(str.isdigit, command))
        if level:
            if int(level) < 0 or int (level) > 10:
                speak("Please specify a valid volume level (1-10).")
            else:
                adjust_volume(level)
    
    # Command: Internet speed test
    elif 'internet speed' in command:
        internet_speed_test()

    # Command: Brigthness
    elif 'brightness' in command:
        change_brightness(command)

    # Command: Full Screen
    elif 'full screen' in command:
        pyautogui.press('f')

    # Command: Full Screen
    elif 'space' in command:
        pyautogui.press('space')

    # Command: (Rewind/Skip)
    elif 'rewind' in command or 'skip' in command or 'jump' in command or 'go back' in command:
        skip_or_rewind(command)

    # Command: Power Manager
    # elif 'sleep' in command or 'hibernate' in command or 'restart' in command or 'shutdown' in command:
    #     power_manager(command)

    # Command: TypeWriter 
    elif 'typewriter' in command:
        manage_keyboard(command)

    # Command: Power Manager
    elif 'turn on' in command or 'turn off' in command or 'room shutdown' in command or 'room startup' in command:
        handle_device(command)
    