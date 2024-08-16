import pyttsx3

class TextToSpeech:
    def __init__(self, rate = 125, voice_index=1):
        self.engine = pyttsx3.init()
        self.set_voice(voice_index)
        self.set_rate(rate)
    
    def set_voice(self, voice_index):
        voices = self.engine.getProperty('voices')
        if 0<=voice_index < len(voices):
            self.engine.setProperty('voice',voices[voice_index].id)
        else:
            raise ValueError("Invalid voice index")
    
    def set_rate(self, rate):
        self.engine.setProperty('rate',rate)
    
    def speak(self,text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"TtS Engine Error: {e}")
