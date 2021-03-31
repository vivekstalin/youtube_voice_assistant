import speech_recognition as sr
import pyttsx3
import requests
import webbrowser as web
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
        print("Exception in jarvis_talk() "+e)

def jarvis_listen():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as talkie:
            playsound('beep_1.mp3')
            print("Listening....")
            voice = listener.listen(talkie,timeout=5)
            command = listener.recognize_google(voice).lower()
            print(command)
            if 'jarvis' in command and 'play' in command:
                command = command.replace('jarvis','').replace('play','').strip()
                jarvis_play(command)
            else:
                jarvis_talk("Sorry I Did not hear you clearly")
                jarvis_talk("Can you please say that again")
    except Exception as e:
        print("Exception in jarvis_listen() "+e)

def jarvis_play(song):
    try:
        song = song.lower().replace('play','').strip()
        jarvis_talk('Playing '+song)
        play_yt(song)
    except Exception as e:
        print("Exception in jarvis_play() "+e)

def play_yt(topic):
    try:
        url = 'https://www.youtube.com/results?q=' + topic
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count - 5] == "/results":
            raise Exception("No video found.")
        web.open("https://www.youtube.com" + lst[count - 5])
        return "https://www.youtube.com" + lst[count - 5]
    except Exception as e:
        print("Exception in play_yt() "+e)

if __name__ == '__main__':
        jarvis_talk()
        jarvis_listen()

