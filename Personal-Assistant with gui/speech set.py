import pyttsx3


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
#print("HELLOO")
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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

speak("hello sir how are you")