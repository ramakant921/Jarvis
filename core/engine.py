import edge_tts
import asyncio
import logging
import os
import sys
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

try:
    from termcolor import colored
except ImportError:
    print("Module 'termcolor' is not installed")

VOICE = "en-US-AvaNeural"
OUTPUT_FILE = "speak.mp3"
    
async def async_speak(speak_text: str, print_text: str = None):
    """Print the given string."""
    print_text = print_text or speak_text
    try:
        cool_text = colored("[Friday] >>>", "cyan", attrs=["bold"])
        print(f'{cool_text} {print_text} \n')
    except:
        print(f'\n[Friday] >>>  {print_text} \n')
    
    """Disabling Bs Logging !todo() (Doesn't Work)"""
    sys.stderr = open(os.devnull, "w")
    logging.getLogger("edge_tts").setLevel(logging.CRITICAL)
    logging.getLogger("pydub").setLevel(logging.CRITICAL)
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)

    """Speak the given audio string."""
    communicate = edge_tts.Communicate(speak_text, VOICE)
    audio_stream = BytesIO()

    async for chunks in communicate.stream():
        if chunks["type"] == "audio":
            audio_stream.write(chunks["data"])
    
    audio_stream.seek(0)
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    play(audio)

def speak(speak_text: str, print_text: str = None):
    asyncio.run(async_speak(speak_text, print_text))
          