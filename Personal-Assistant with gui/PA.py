from asyncio import Task, tasks
from cProfile import label
from modulefinder import IMPORT_NAME
from re import S
from typing_extensions import Self
from urllib import request
import pyttsx3
from scipy.misc import face
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyautogui as p
import sys
import os
from os import name, startfile, system
from pydoc import cli 
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
import requests
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisGui import Ui_JarvisUI
import cv2

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
#print("HELLOO")
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dict_apps={"Command prompt":"cmd","paint":"paint","chrome":"chrome","excel":"excel","word":"winword","whatsapp":"whatsApp"}    

def initial():
    speak("Starting session")
    print("Starting session")
    speak("initializing session")
    print("initializing session")
    speak("collecting and compiling requirements ")
    print("collecting and compiling requirements")
    speak("checking cpu and gpu")
    print("checking cpu and gpu")
    speak("all set now!!")
    print("all set now!!")

def Wishme():
    speak("Starting session")
    print("Starting session")
    speak("initializing session")
    print("initializing session")
    speak("collecting and compiling requirements ")
    print("collecting and compiling requirements")
    speak("checking cpu and gpu")
    print("checking cpu and gpu")
    speak("all set now!!")
    print("all set now!!")
    hour=int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    if hour>=0 and hour<12:
        speak(f"Good Morning  sir , wake up jaaan its {strTime}")
        print(f"Good Morning  sir ,  its {strTime}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon  sir  , wake up  its already  {strTime}")
        print(f"Good Afternoon  sir  , wake up   its already  {strTime}")

    elif hour>=18 and hour<24:
        speak(f"good evening  sir , its {strTime} ")
        print(f" Good evening  sir, its  {strTime}")

    
    speak("  Please tell me how may i help you")    
    print("Please tell me how may i help you")        






def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']

    return city, state,country

def open_app (query):
    speak("Launching sir ")
    #if ".com" in self.query or ".co.in" or ".org" in self.query:
     #   self.query=self.query.replace("open","")
     #   self.query=self.query.replace("jarvis","")
      #  self.query=self.query.replace("launch","")
       # self.query = self.query.replace(" ","")
       # webbrowser.open(f"https://www.{self.query}")
    apps=list(dict_apps.keys())
    for app in apps:
        if app in query:
            os.system(f"start  {dict_apps[app]}")

def close_app(query):
    speak("Closing sir")
    apps=list(dict_apps.keys())
    for app in apps:
        if app in query:
            os.system(f"taskkill /f /im {dict_apps[app]}.exe")
    

def whatsapp(name,message):
    startfile("C:\\Users\\DHRUV SAINI\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=391, y=127)
    sleep(2)
    write(name)
    sleep(1)
    click(x=238, y=308)
    sleep(1)
    click(x=978, y=1034)
    sleep(1)
    write(message)
    press("enter")

def whatsapp_call(name):
    startfile("C:\\Users\\DHRUV SAINI\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(14)
    click(x=401, y=129)
    sleep(2)
    write(name)
    sleep(2)
    click(x=238, y=308)
    sleep(2)
    click(x=1712, y=62)
    press("enter")

def Notepad():
    speak("Tell me the self.query sir!! ")
    speak("i am ready to write  sir ")
    writes = takeCommand()

    time =(datetime.datetime.now().strftime("%H:%M:%S"))
    filename= str(time).replace(":","-") + ".note.txt"

    with open(filename,"w") as file:
        file.write(writes)
    path_1 ="D:\\JARVIS\\" + str(filename)
    path_2 ="D:\\JARVIS\\Database\\Notepad_Data\\" + str(filename)
    os.rename(path_1,path_2)
    os.startfile(path_2)

def takeCommand():
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
        self.Task()
    
    def takeCommand(self):
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

        
        

    def Task(self):
            Wishme()
            

            while True:
                


                self.query =self.takeCommand().lower()

                if 'wikipedia' in self.query:
                        speak("Searching Wikipedia... ")
                        self.query = self.query.replace("wikipedia","")
                        results= wikipedia.summary(self.query,sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                
                elif 'open youtube' in self.query:
                        webbrowser.open("youtube.com")

                elif 'open google' in self.query:
                    speak("Sir, What should i search on google")
                    tm = self.takeCommand().lower()
                    webbrowser.open(f"{tm}")
                        

                elif 'the time' in self.query:
                        strTime1 = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"SIr ,THe TIme is  {strTime1}") 

                elif 'play' in self.query:
                        song = self.query.replace('play', '')
                        speak('playing ' + song)
                        pywhatkit.playonyt(song)

                elif 'date' in self.query:

                    speak("No  Sorry for that    as    i am having  headache")

                elif "are you single" in self.query:
                    speak("No  i am having relationship with wifi")    


                    
                elif "launch" in self.query:
                    speak("Sir, tell me the name of the website !!")
                    web=self.takeCommand()
                    web='https://www.'+web+'.com'
                    webbrowser.open(web)

                elif "shut up" in self.query:
                    speak("Thanks for using me sir, have a good day") 
                    speak("Good night sir , take care")
                    break
                    

                elif "send whatsapp message" in self.query:
                    speak("please tell me name of the person sir:")
                    name=self.takeCommand()
                    print(f"Name of the person: {name} ")
                    speak("Tell me the message sir:")
                    message=self.takeCommand()
                    print(message)
                    
                    whatsapp(name,message)

                elif "call" in self.query:
                    speak("please tell me the name of the person:")
                    name=self.takeCommand()
                    speak(f"Calling  {name} ")
                    whatsapp_call(name)  
                        

                elif "open" in self.query:
                    open_app(self.query)
                        
                elif "close" in self.query:
                    close_app(self.query)
                        
                elif "increase" in self.query:
                    p.press('volumeup')
                    speak("increased sir")

                elif "decrease" in self.query:

                    p.press('volumedown') 
                    speak("decreased sir")

                elif "mute" in self.query:
                    p.press("volumemute")
                    speak("muted sir")         

                        


                elif "online class" in self.query:
                    speak("which class you want to attend sir:")
                    print("which class you want to attend sir:")
                    online_class_attend=self.takeCommand()
                    if "science" in online_class_attend:
                        from ONLINE_CLASS.LINK import science 
                        Link = science()
                        webbrowser.open(Link)
                        sleep(10)
                        click(x=630, y=787)
                        sleep(1)
                        click(x=720, y=792)
                        sleep(2)
                        click(x=1364, y=565)
                        speak("Link joined sir")
                                
                    elif "maths" in online_class_attend:
                                from ONLINE_CLASS.LINK import maths 
                                Link = maths()
                                webbrowser.open(Link)
                                sleep(10)
                                click(x=630, y=787)
                                sleep(1)
                                click(x=720, y=792)
                                sleep(2)
                                click(x=1364, y=565)
                                speak("Link joined sir")
                            
                elif "write" in self.query:
                        Notepad()

                elif "where i am" in self.query or "current location" in self.query or "where am i" in self.query:

                    my_location()
                    try:
                        city, state, country = my_location()
                        print(f" Sir your city is {city}")
                        print(f" Sir your state is {state}")
                        print(f" Sir your country is {country}")
                        speak(f"You are currently in {city} city which is in {state} state and country {country}")
                    except Exception as e:
                        speak("Sorry sir, I coundn't fetch your current location. Please try again")  

   # if __name__=="__main__":
    #    Wishme()
     #   Task()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie =QtGui.QMovie("C:/Users/DHRUV SAINI/Dropbox/PC/Downloads/G.U.I Material-20220114T141917Z-001/G.U.I Material/B.G/Black_Template.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie =QtGui.QMovie("C:/Users/DHRUV SAINI/Dropbox/PC/Downloads/G.U.I Material-20220114T141917Z-001/G.U.I Material/B.G/Iron_Template_1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie =QtGui.QMovie("C:/Users/DHRUV SAINI/Dropbox/PC/Downloads/G.U.I Material-20220114T141917Z-001/G.U.I Material/VoiceReg/__1.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie =QtGui.QMovie("C:/Users/DHRUV SAINI/Dropbox/PC/Downloads/G.U.I Material-20220114T141917Z-001/G.U.I Material/ExtraGui/initial.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie =QtGui.QMovie("C:/Users/DHRUV SAINI/Dropbox/PC/Downloads/G.U.I Material-20220114T141917Z-001/G.U.I Material/ExtraGui/Health_Template.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)    

        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        #self.ui.textBrowser.setText(label_date)
        #self.ui.textBrowser_2.setText(label_time)


app =QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
    