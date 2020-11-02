
import calc
import operator
import smtplib 
import requests, json 
from datetime import datetime
from datetime import date
import speech_recognition as sr 
import pyttsx3
from pygame import mixer  
from imageai.Detection import ObjectDetection
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import readmail
import whatsapp
import API_list as API


def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
	
SpeakText("Welcome to the voice, your personal assistant")
'''detector = ObjectDetection()

model_path = "./model/yolo-tiny.h5"
input_path = "./input/NewPicture.jpg"
output_path = "./output/newimage.jpg"

detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
import cv2

videoCaptureObject = cv2.VideoCapture(0)'''







main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Chennai"
API_KEY = "87950af400adc37ba457d4bd7bc07a27"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

emaildb={
        "jackson":"siddharth.dash07@gmail.com",
        "jonathan":"siddharth.d.wisekreator@gmail.com"
        
        }

whatsappdb={
        "siddharth":"+919176136743"
        
        }


r = sr.Recognizer() 



	


while(1):
    
    '''menu for tasks'''
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
        if "read" in a and "email" in a:
            readmail.readmymail()    
#sending email
        elif "email" in a:
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login("siddhu.dash@gmail.com", "65477412") 
            SpeakText("Please say the receiver's name")
            
            try:
                with sr.Microphone() as source2:
                    audio2 = r.listen(source2)
                    receive = r.recognize_google(audio2)
                    print(receive)
            except sr.UnknownValueError:
                SpeakText("message was not clear")
            if receive.lower() in emaildb:
                receive=receive.lower()
                emailid=emaildb[receive]
                SpeakText("Please say your message")           
                try:
                    with sr.Microphone() as source2:
                        audio2 = r.listen(source2)
                        message = r.recognize_google(audio2)
                except sr.UnknownValueError:
                    SpeakText("message was not clear")
                SpeakText("Sending")
                s.sendmail("siddhu.dash@gmail.com", emailid, message) 
                s.quit() 
                
                print("email sent")

#weather info
        elif "weather" in a:
            API.weather_api()
               
        elif "news" in a:
            API.news_api()
        elif "time" in a:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            SpeakText(current_time)
        elif "date" in a:
            today = date.today() 
            print("Today date is: ", today)
            SpeakText(today)
        elif "calculator" in a:
            calc.calculator()
        elif "song" in a or "music" in a:
            try:
                with sr.Microphone() as source2:
                    SpeakText("what song would you like to hear")
                    audio2 = r.listen(source2)
                    
                    song_name = r.recognize_google(audio2)
                    song_name=song_name.lower()
                    
            except sr.UnknownValueError:
                SpeakText("message was not clear")
            mixer.init() 
            SpeakText("Press P to pause.")
            SpeakText("Press r to Resume.")
            SpeakText("Press e to exit music player.")
            mixer.music.load("./songs/"+song_name+".mp3") 
            mixer.music.set_volume(0.7) 
            mixer.music.play() 
            while True: 
                  
                print("Press 'p' to pause, 'r' to resume") 
                print("Press 'e' to exit the program") 
                query = input("  ") 
                  
                if query == 'p': 
                    mixer.music.pause()      
                elif query == 'r': 
                    mixer.music.unpause() 
                elif query == 'e': 
                    mixer.music.stop() 
                    break
        elif "detect" in a:
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("./input/NewPicture.jpg",frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
            for eachItem in detection:
                print(eachItem["name"] , " : ", eachItem["percentage_probability"])
        elif "whatsapp" in a:
            SpeakText("Who is the receiver")
            try:
                with sr.Microphone() as source2:
                    audio2 = r.listen(source2)
                    receive = r.recognize_google(audio2)
                    print(receive)
            except sr.UnknownValueError:
                SpeakText("message was not clear")
            
            if receive.lower() in whatsappdb:
                receive=receive.lower()
                phno=whatsappdb[receive]
                SpeakText("say your message")
                try:
                    with sr.Microphone() as source2:
                        audio2 = r.listen(source2)
                        message = r.recognize_google(audio2)
                        print(message)
                except sr.UnknownValueError:
                    SpeakText("message was not clear")
                
                whatsapp.whatsappmsg(message,phno)
            else:
                SpeakText("receiver not available")
            
        
        
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    