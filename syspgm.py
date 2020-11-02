import os 
import wolframalpha
from selenium import webdriver 
import speech_recognition as sr 
import pyttsx3
from pygame import mixer  
import pyttsx3
def SpeakText(command): 
	

	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
    

num = 1

# function used to open application 
# present inside the system. 
def open_application(a):
    
    print("now here")
    if "chrome" in a or "browser" in a:
        SpeakText("Opening Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
    elif "firefox" in a or "mozilla" in a:
        SpeakText("Opening Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
    else:
        return




# Driver Code 
def openfile():
    r = sr.Recognizer()
    print("Inhere   sfsghd" )
    SpeakText("Welcome to app explorer say open app name to open it")
    SpeakText("Close to exit")
    while(True):
            
        try:
            with sr.Microphone() as source2:
                print("noise redn")
                r.adjust_for_ambient_noise(source2, duration=0.5)
                print("listening")
                audio2 = r.listen(source2)
                print("converting")
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Did you say "+MyText)
                
                a = MyText.split(" ")
                print(a)
            
            if "open" in a:
                open_application(a)
            if "close" in a:
                return
    
    
                
            
            
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
            
        