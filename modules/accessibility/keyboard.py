from core.engine import speak
import pyautogui

def typewriter(text):
    if not text:
        return
    speak("writing", f'writing: {text}')
    pyautogui.write(text, interval=0.015)

# main function: receive command
def manage_keyboard(command):
    if 'typewriter' in command:
        typewrite_text = command.replace('typewriter', '').strip()
        typewriter(typewrite_text)