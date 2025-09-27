#pyttsx3 is a text-to-speech conversion library.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello World")
engine.runAndWait()