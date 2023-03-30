from typing_extensions import Self
from JarvisGui import Ui_JarvisUI
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from modulefinder import IMPORT_NAME
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import sys
import os
from os import name, startfile
from pydoc import cli 
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
#print("HELLOO")
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',140)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand(self):
    # It takes microphone input from the user 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print(e)    
        print("Say that again please...")  
        return "None"
    return query    

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Task_EXE()



    def Wishme(self):
        hour=int(datetime.datetime.now().hour)
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        if hour>=0 and hour<12:
            speak(f"Good Morning  darlingg , wake up jaaan its {strTime}")
            print(f"Good Morning  Darlingg ,  its {strTime}")

        elif hour>=12 and hour<18:
            speak(f"Good Afternoon  darlingg  , wake up  its already  {strTime}")
            print(f"Good Afternoon  Darlingg  , wake up   its already  {strTime}")

        elif hour>=18 and hour<24:
            speak(f"good evening  Baby , its {strTime} ")
            print(f" Good evening  Baby, its  {strTime}")

        
        speak("  Please tell me how may i help you")    
        print("Please tell me how may i help you")        


    
    #if __name__=="__main__":

    #    Wishme()
        

        def Task_EXE(self):
            while True:
                if __name__=="__main__":

                    self.query=self.takeCommand().lower()


                    if 'wikipedia' in self.query:
                        speak("Searching Wikipedia... ")
                        query = query.replace("wikipedia","")
                        results= wikipedia.summary(query,sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                
                    elif 'open youtube' in self.query:
                        webbrowser.open("youtube.com")

                    elif 'open google' in self.query:
                        speak("Sir, What should i search on google")
                        tm = takeCommand().lower()
                        webbrowser.open(f"{tm}")
                        

                    elif 'the time' in self.query:
                        strTime1 = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"SIr ,THe TIme is  {strTime1}") 

                    elif 'play' in self.query:
                        song = query.replace('play', '')
                        speak('playing ' + song)
                        pywhatkit.playonyt(song)

                    elif 'date' in self.query:
                        speak("No  Sorry for that    as    i am having  headache")

                    elif "are you single" in self.query:
                        speak("No  i am having relationship with wifi") 


StartFunctions= MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_JarvisUI
        self.jarvis_ui.setupUi(Ui_JarvisUI,JarvisUI) -> None
        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)


    def startFunc(self):
        self.jarvis_ui.movies_label_2 = QtGui.QMovie("Iron_Template_1.gif")
        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_label_2)
        self.jarvis_ui.movies_label_2.start()

        self.jarvis_ui.movies_label_3 = QtGui.QMovie("__1.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_label_3)
        self.jarvis_ui.movies_label_3.start()


        self.jarvis_ui.movies_label_4 = QtGui.QMovie("initial.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_label_4)
        self.jarvis_ui.movies_label_4.start()

        self.jarvis_ui.movies_label_5 = QtGui.QMovie("Health_Template.gif")
        self.jarvis_ui.label_5.setMovie(self.jarvis_ui.movies_label_5)
        self.jarvis_ui.movies_label_5.start()

        StartFunctions.start()


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())