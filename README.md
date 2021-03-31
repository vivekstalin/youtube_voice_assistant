## Getting Started
Hey Guys! I am giving this project as an idea to develop a simple and super cool voice assistant bot that can play something for you on youtube when you speak to it

### Prerequisites

Doesn't need much except Python and few Python Packages
* Python
  ```
  python version 3.5+
  ```
* Python Packages
  ```
  1. SpeechRecognition
  2. pyttsx3
  3. playsound
  4. Basic packages like requests, webbrowser which should available by default (install only if shows any error)
  
  Use your python pip to install these packages - pip install <packagename>
  ```
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/vivekstalin/youtube_voice_assistant.git
   ```
## Usage
I have kept the code open and it is visible for you in .py format

**Clone it, Fork it, Modularize it and Extended it to make your own bot**
 
The sample version I have put here works in the below way:
```
1. Run the main file ~/src/voice.py
2. It would start taking to you. My Bot name is Jarvis
3. Ask you to talk after beep, So once you hear the beep wait for one or two seconds and then talk 
   Voice Input Format: <bot name> <play> <content in youtube>
   Ex1: Jarvis play faded song
   Ex2: Jarvis play Falcon heavy test flight
4. There you go, it will take few seconds for the search to happen in the background and then you will see the youtube video getting played automatically on youtube in the browser
```

