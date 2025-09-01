import wikipedia
from core.engine import speak

def search_wikipedia(query):
    """Search Wikipedia for the given query and read the summary."""
    try:
        speak("Searching Wikipedia...")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("The query is ambiguous. Please provide more specific information.")
    except Exception:
        speak("I couldn't fetch Wikipedia results. Please try again later.")