import speech_recognition as sr
from text_to_speech import TextToSpeech
from news import fetch_latest_news
from commands import process_command

def listen_for_wake_word(recognizer, tts):
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
            print("Recognizing...")
            wake_word = recognizer.recognize_google(audio).lower()
            print("audio was:",wake_word )
            return wake_word
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def listen_for_command(recognizer):
    try:
        with sr.Microphone() as source:
            print("Waiting for command...")
            audio = recognizer.listen(source,timeout = 2,phrase_time_limit = 3)
            print("Recognizing command...")
            command = recognizer.recognize_google(audio)
            print("Command given was :",command)
            return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main():
    tts = TextToSpeech()
    tts.speak("Starting John")
    recognizer = sr.Recognizer()

    while True:
        wake_word = listen_for_wake_word(recognizer, tts)
        if wake_word and "john" in wake_word:
            tts.speak("Yes Sir")
            command = listen_for_command(recognizer)
            if command:
                process_command(command)

if __name__ == "__main__":
    main()
    