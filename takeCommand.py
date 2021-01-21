import speech_recognition as sr
from time import sleep

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print("say that again please...")
        return "None"

    return query.lower()