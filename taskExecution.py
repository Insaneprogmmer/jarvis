import sys
from time import sleep

from takeCommand import takeCommand
import time_module
from speak import speak
import _thread


def taskExecution():

    while True:
        command = takeCommand()

        if 'what is time' in command:
            speak(f'Time is{time_module.getTime()}')

        elif 'sleep jarvis' in command:
            speak('Yes sir, you can call again')
            break

        elif 'goodbye jarvis' in command:
            speak("goodbye sir, see you again")
            sys.exit()
