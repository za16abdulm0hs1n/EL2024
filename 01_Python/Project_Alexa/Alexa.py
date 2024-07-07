import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import random
import speech_recognition as sr
import threading

class VoiceAssistant:
    recognizer = sr.Recognizer()

    def record_audio(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio

    def recognize_speech(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""

    def respond(self, response):
        tts = gTTS(text=response, lang='en')
        filename = "response.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def process_commands(self, command):
        if 'your name' in command:
            self.respond("My name is Alexa.")
        elif 'time' in command:
            self.respond(ctime())
        elif 'search' in command:
            search_query = command.replace('search', '')
            url = f"https://www.google.com/search?q={search_query.strip()}"
            webbrowser.open(url)
            self.respond(f"Here is what I found for {search_query}.")
        elif 'exit' in command:
            self.respond("Goodbye!")
            exit()
        else:
            self.respond("Sorry, I didn't get that. Can you please repeat?")

    def start(self):
        print("Alexa is starting...")
        while True:
            audio = self.record_audio()
            command = self.recognize_speech(audio)
            if command:
                self.process_commands(command)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.start()
