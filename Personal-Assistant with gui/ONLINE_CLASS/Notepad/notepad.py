


from datetime import datetime


def Notepad():
    speak("Tell me the query sir!! ")
    speak("i am ready to sir ")
    writes= TakeCommand()

    time = int(datetime.now().strftime("%H:%M:%S"))
    filename= str(time).replace(":","-") + ".note.txt"
    with open(filename,"w") as file:
        file.write(writes)
    path_1 = ("D:\\JARVIS\\ONLINE_CLASS\\Notepad\\") + str(filename)
    path_2 = ("D:\\JARVIS\\Database\\Notepad_Data\\") + str(filename)
    os.rename(path_1,path_2)
    os.startfile(path_2)

