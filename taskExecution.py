import sys
from takeCommand import takeCommand
import time_module
from speak import speak

import json

with open('jarvis.json') as f:
    data = json.load(f)


def commandFounder(command):
    for a in data["intents"]:
        for b in a["pattern"]:
            if command == b:
                result = str(a['answer'])[1:-1]
                return result


def taskExecution():
    while True:
        command = takeCommand()

        founder = commandFounder(command)

        if 'what is time' in founder:
            speak(f'Time is{time_module.getTime()}')

        elif 'sleep jarvis' in command:
            speak('Yes sir, you can call again')
            break

        elif 'goodbye jarvis' in command:
            speak("goodbye sir, see you again")
            sys.exit()
