import speech_recognition as sr
import pyttsx3
import pywhatkit
from playsound import playsound

def jarvis_talk(text=''):
    try:
        jarvis = pyttsx3.init()
        if text == '':
            jarvis.say("Hi")
            jarvis.say("I am jarvis")
            jarvis.say("I am vivek's youtube voice assistant")
            jarvis.say("Tell me what can I search for you in youtube")
            jarvis.say("say that after the beep")
        else:
            jarvis.say(text)
        jarvis.runAndWait()
    except Exception as e:
        print("Exception "+e)

def jarvis_listen():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as talkie:
            playsound('beep_1.mp3')
            print("Listening....")
            voice = listener.listen(talkie,timeout=7)
            command = listener.recognize_google(voice).lower()
            print(command)
            if 'jarvis' in command and 'play' in command:
                command = command.replace('jarvis','').replace('play','').strip()
                jarvis_play(command)
            else:
                jarvis_talk("Sorry I Did not hear you clearly")
                jarvis_talk("Can you please say that again")
    except Exception as e:
        print("Exception "+e)

def jarvis_play(song):
    try:
        song = song.lower().replace('play','').strip()
        jarvis_talk('Playing '+song)
        pywhatkit.playonyt(song)
    except Exception as e:
        print("Exception "+e)

if __name__ == '__main__':
        jarvis_talk()
        jarvis_listen()

