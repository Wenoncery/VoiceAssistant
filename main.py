import pyjokes as pyjokes
import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
import os
from pydub import AudioSegment
from pydub.playback import play
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# specify the path to the directory that contains your songs
path = r"C:\Users\rares\PycharmProjects\VoiceAssistant\Songs"

AudioSegment.converter = r"C:\Users\rares\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"

John = 555 # Comment

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def play_song(song_name):
    song_path = os.path.join(path,song_name)
    if os.path.isfile(song_path):
        song = AudioSegment.from_file(song_path, format="wav")
        play(song)
        speak("Playing "+song_name)
    else:
        speak("Sorry, the song "+song_name+" is not found")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Now listening")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Deciphering")
            command = r.recognize_google(audio, language ='en-in')
            print("You Said: " + command)
        except Exception as e:
            print(e)
            print("Did not hear anything")
            return "None"
    return command


while True:
    command = take_command().lower()
    if 'exit' in command:
        speak("Exiting the program")
        break
    # Conversational
    if 'how are you' in command:
        speak("I'm doing well")
    if 'thank you' in command:
        speak("Anytime")

    # Tasks
    if 'time' in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak("The Current Time is " + current_time)
    if 'random number' in command:
        randInt = random.randint(0, 10)
        speak("A random number between 0 and 10 is " + str(randInt))
    if 'open notepad' in command:
        os.system("notepad")
        speak("Opening Notepad")
    if 'play music' in command or "play song" in command:
        # song_name = command.split('play music',1)[1].strip()
        # play_song(song_name)
        speak("Here you go with music")
        # music_dir = "G:\\Song"
        music_dir = r"C:\Users\rares\PycharmProjects\VoiceAssistant\Songs"
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[1]))

    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    if 'open youtube' in command:
        speak("Here you go to Youtube\n")
        url1 = "youtube.com"
        firefox = webbrowser.Mozilla(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        firefox.open_new(url1)

    if 'open browser' in command:
        codePath = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        os.startfile(codePath)

    if 'tell me a joke' in command:
        speak(pyjokes.get_joke())

    if "why you came to world" in command:
        speak("Thanks to Rares. Further it's a secret")

