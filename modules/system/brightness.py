from core.engine import speak
import screen_brightness_control as sbc



def set_brightness_level(level):
    """
    Sets brightness to the specified level for physical monitors.
    """
    try:
        sbc.set_brightness(level)
        speak(f"Brightness set to {level}%")
    except Exception as e:
        speak("Failed to set brightness.",
              f"Error setting brightness: {e}")

def increase_brightness():
    """
    Increases brightness by 10% for physical monitors.
    """    
    try:
        sbc.set_brightness('+10')
        speak("Brightness increased by 10%")
    except Exception as e:
        speak("Failed to increase brightness.",
              f"Error increasing brightness: {e}")

def decrease_brightness():
    """
    Decreases brightness by 10% for physical monitors.
    """
    try:
        sbc.set_brightness('-10')
        speak("Brightness decreased by 10%")
    except Exception as e:
        speak("Failed to decrease brightness.", 
              f"Error decreasing brightness: {e}")

def change_brightness(command):
    """
    Adjusts brightness based on the given command.
    """
    try:
        level = ''.join(filter(str.isdigit, command))
        if level:
            set_brightness_level(level)
        elif "increase" in command:
            increase_brightness()
        elif "decrease" in command:
            decrease_brightness()
        else:
            speak("Invalid brightness command.")
    except Exception as e:
        speak("An error occurred while processing the brightness command.", 
        f"An error occurred while processing the brightness command: {e}")
