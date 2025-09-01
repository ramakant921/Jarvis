from core.engine import speak
import requests

relay_url = 'http://localhost:6969/relay'
protocol_url = 'http://localhost:6969/protocol'

def handle_device(command):
    if 'light' in command:
        print("Toggling light")
        speak("Toggling light")
        requests.get(f'{relay_url}/1/toggle')

    elif 'fan' in command:
        print("Toggling fan")
        speak("Toggling fan")
        requests.get(f'{relay_url}/2/toggle')
        
    elif 'startup' in command:
        print("Protocol 1 initiated...")
        speak("initializing startup protocol")
        requests.get(f'{protocol_url}/1')
        
    elif 'shutdown' in command:
        print("Protocol 0 initiated...")
        speak("initializing shutdown protocol")
        requests.get(f'{protocol_url}/0')

    else:
        print("I don't know what hit me", command)
        