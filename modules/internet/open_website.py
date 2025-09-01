import webbrowser
from core.engine import speak
from sys import platform

LINUX_BROWSER = 'firefox'
WINDOWS_BROWSER = 'chrome'

def open_this_thing(url, name):
    try:
        if platform == 'linux' or platform == 'linux2':
            webbrowser.register(LINUX_BROWSER, None, webbrowser.BackgroundBrowser("/usr/bin/firefox"))
            webbrowser.get(LINUX_BROWSER).open(url)
        elif platform == 'win': 
            webbrowser.register(WINDOWS_BROWSER, None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get(WINDOWS_BROWSER).open(url)
        speak(f"Opening {name}.")
    except Exception as e:
        print(f"Error opening {name}: {e}")
        speak(f"Couldn't open {name}. Please check your browser path or network.")

def open_website(command):
    """Open a website in Chrome."""
    
    if "youtube" in command:
        open_this_thing("https://youtube.com", "Youtube")
    elif 'google' in command:
        open_this_thing("https://google.com", "Google")
    elif 'whatsapp' in command:
        open_this_thing("https://web.whatsapp.com", "Whatsapp")
    elif 'chat' in command:
        open_this_thing("https://chatgpt.com", "ChatGPT")

    