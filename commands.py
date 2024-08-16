import webbrowser
import musiclibrary
from news import fetch_latest_news
from text_to_speech import TextToSpeech
from client import ai_reply

tts = TextToSpeech()

def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif command.startswith("play"):
        song = command.split()[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            tts.speak("Sorry, I couldn't find that song in the song library.")
    elif "news" in command:
        articles = fetch_latest_news()
        if articles:
            for article in articles:
                tts.speak(article["title"])
        else:
            tts.speak("Sorry, I couldn't fetch the news right now.")
    else:
        tts.speak(ai_reply(command))