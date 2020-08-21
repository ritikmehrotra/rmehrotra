import pyttsx3
import os
pyttsx3.speak("could you please type your name below")
name = input("please enter your name here : ")
pyttsx3.speak("Hello" + name + "welcome to my software")
pyttsx3.speak("Can you write the name of the application below? My software will launch it for you")
while True:
    a=input("Enter the application you would like to open : ")
    if (("run" in a) or ("execute" in a)) and (("notepad" in a) or ("text editor" in a)):
        print("opening your text editor!!!")
        os.system("notepad")
        
    elif (("run" in a) or ("open" in a) or ("start" in a)) and (("chrome" in a) or ("browser" in a)):
        print("opening your browser!!!!!!")
        os.system("start chrome")
        
    elif (("run" in a) or ("open" in a) or ("start" in a)) and (("microsoft edge" in a) or ("browser" in a)):
        print("opening your browser!!!!!!")
        os.system("microsoftedge")
        
    elif (("run" in a) or ("open" in a) or ("start" in a)) and (("mozilla firefox" in a) or ("browser" in a)):
        print("opening your browser!!!!!!")
        os.system("mozillafirefox")
        
    elif (("run" in a) or ("open" in a) or  ("start" in a)) and (("windows media player" in a) or ("music player" in a)):
        print("opening your media player!!!!")
        os.system("wmplayer")
        
    elif (("run" in a) or ("open" in a) or  ("start" in a)) and ("calculator" in a):
        print("opening your calculator!!!!!")
        os.system('calc.exe')
        
    elif (("run" in a) or ("open" in a) or ("start" in a)) and ("wordpad" in a):
        print("opening your wordpad!!!!!!")                                                            
        os.system('write.exe')
        
    elif  ("exit" in a)  or ("quit" in a):
        break

    else:
        print("Sorry , doesn't support")