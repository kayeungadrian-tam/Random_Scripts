from cProfile import run
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            # voice = listener.listen(source)
            voice = listener.record(source, duration=5)
            command = listener.recognize_google(voice)
            command = command.lower()


            if command:
                print("SHIT------------------------")


            # if 'alexa' in command:
            #     command = command.replace('alexa', '')
            #     print(command)
    except:
        pass
    return command




def run_alexa():
    try:
        command = take_command()
    except:
        command = "OH NO!"

    print(command)
while True:
    run_alexa()