from core.engine import speak
from termcolor import colored
import datetime
import time
import sys

def wish_me():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir!")
    else:
        speak("Good Evening, sir!")

#don't know what to do with the param hehehe
def listening_animated_text(animation_event):
    """Display animated text with dots in the terminal"""
    text = "Listening"
    dot_count=3
    delay=0.4
    current_dots = 0
    while True:
        dots = "." * current_dots  # Generate the dots dynamically
        sys.stdout.write(f"\r{colored(text, "red", attrs=['bold'])}{dots}{' ' * (dot_count - len(dots))}")  # Clear previous output
        sys.stdout.flush()
        time.sleep(delay)
        
        current_dots = (current_dots + 1) % (dot_count + 1)  # Reset to 0 after reaching dot_count
