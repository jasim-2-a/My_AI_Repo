import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)  
        print(f"Your command: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError:
        print("Sorry, I am having trouble connecting to the speech recognition service.")
        return None


def execute_command(command):
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    
    elif 'time' in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"The current time is {current_time}")
    
    elif 'date' in command:
        today = datetime.datetime.today()
        current_date = today.strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    
    elif 'wikipedia' in command:
        speak("What would you like to know about?")
        query = listen()
        if query:
            speak("Searching Wikipedia...")
            try:
                summary = wikipedia.summary(query, sentences=1)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("I found multiple results. Please be more specific.")
            except wikipedia.exceptions.HTTPTimeoutError:
                speak("I couldn't connect to Wikipedia. Please check your internet connection.")
    
    elif 'open' in command:
        if 'youtube' in command:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        elif 'google' in command:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        else:
            speak("Sorry, I can only open YouTube or Google for now.")
    
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye! Have a great day!")
        exit()
    
    else:
        speak("Sorry, I didn't understand that command. Please try again.")


def run_assistant():
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        command = listen()
        if command:
            execute_command(command)


run_assistant()
