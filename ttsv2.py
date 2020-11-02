import keyboard
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
import music_player as music
import emailAPI
import sms
import helpdesk
import VA_settings as settings
import syspgm
from tkinter import *                       


def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
def get_operator_fn(op):
    return {
        'plus':operator.add,    
        '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                'divided' :operator.__truediv__,
                'Mod' : operator.mod,
                'mod' : operator.mod,
                '^' : operator.xor,
                'into':operator.mul,
                'times':operator.mul,
                }[op]
def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


#SpeakText("Welcome to the voice, your personal assistant")
#SpeakText("How may I help you?")

detector = ObjectDetection()

model_path = "./model/yolo-tiny.h5"
input_path = "./input/NewPicture.jpg"
output_path = "./output/newimage.jpg"

detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
import cv2

videoCaptureObject = cv2.VideoCapture(0)







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
        "shantanu":"+916362633064",
        "siddharth":"+919176136743",
        "neetigya":"+917599315938"
        
        }

account_sid = 'ACc1669714d56720604633d46a1b99e30a'
auth_token = '248aa4f9f31d1c7f694ab548f7fa1606'


r = sr.Recognizer() 




    
'''menu for tasks'''
def main():
    try:
       with sr.Microphone() as source2:
            print("noise redn")
            
            r.adjust_for_ambient_noise(source2, duration=0.5)
            print("listening")
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Vision: " + "listening" + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            audio2 = r.listen(source2)
            print("converting")
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say "+MyText)
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + str(MyText) + '\n\n')
            ChatLog.config(foreground="#145465", font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
         
            
            a = MyText.split(" ")
            print(a)
            
       if "read" in a and "email" in a:
           content=readmail.readmymail()    
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "Vision: subject: " + str(content[0]) + '\n\n')
           ChatLog.insert(END, "Vision: from: " + str(content[1]) + '\n\n')
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)
    
       elif "email" in a:
           
           s = smtplib.SMTP('smtp.gmail.com', 587) 
           s.starttls() 
           s.login("siddhu.dash@gmail.com", "65477412") 
           SpeakText("Please say the receiver's name")
           receive="did not get"
           message="not clear"
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "Vision: " + "Please say the receiver's name" + '\n\n')
           
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END) 
           try:
               with sr.Microphone() as source2:
                   audio2 = r.listen(source2)
                   receive = r.recognize_google(audio2)
                   print(receive)
           except sr.UnknownValueError:
               SpeakText("message was not clear")
           
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "You: " + receive + '\n\n')
           
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END) 
           
           
           if receive.lower() in emaildb:
               receive=receive.lower()
               emailid=emaildb[receive]
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "vision: " + "please say your message" + '\n\n')
           
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)  
           SpeakText("Please say your message")           
           try:
               with sr.Microphone() as source2:
                   audio2 = r.listen(source2)
                   message = r.recognize_google(audio2)
           except sr.UnknownValueError:
                SpeakText("message was not clear")
           
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "You: " + message + '\n\n')
           
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)  
           
           SpeakText("Sending")
           s.sendmail("siddhu.dash@gmail.com", emailid, message) 
           s.quit() 
                
           print("email sent")
           SpeakText("email sent")
           
       elif "help" in a or "helpdesk" in a:
           helpdesk.helpdesk()
       elif "settings" in a or "adjust" in a or "setting" in a:
           settings.settings()
    
       elif "weather" in a:
           report=API.weather_api()
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "Vision: city: " + report[0] + '\n\n')
           ChatLog.insert(END, "Vision: temperature: " + report[1] + '\n\n')
           ChatLog.insert(END, "Vision: humidity: " + report[2] + '\n\n')
           ChatLog.insert(END, "Vision: pressure: " + report[3] + '\n\n')
           ChatLog.insert(END, "Vision: forecast: " + report[4] + '\n\n')
           
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)
           
       elif "app" in a or "application" in a:
           syspgm.openfile()
    
                  
    
       elif "news" in a or "new" in a:
           results=API.news_api()
           for i in range(len(results)-5):
               print(i+1,results[i])
               SpeakText(results[i])
               ChatLog.config(state=NORMAL)
               ChatLog.insert(END, "Vision: " + str(results[i]) + '\n\n')
               ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
               ChatLog.config(state=DISABLED)
               ChatLog.yview(END)
       elif "time" in a:
           now = datetime.now()
           current_time = now.strftime("%H:%M:%S")
           SpeakText(current_time)
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "Vision: " + str(current_time) + '\n\n')
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)
    
       elif "date" in a or "day" in a:
    
    
           today = date.today() 
           print("Today date is: ", today)
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "Vision: " + str(today) + '\n\n')
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)
                              
           SpeakText(today)
       elif "calculator" in a:
           calc.calculator()
          
       elif "song" in a or "music" in a:
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "Vision: " + "Press P to pause." + '\n')
           ChatLog.insert(END, "Vision: " + "Press r to Resume." + '\n')
           ChatLog.insert(END, "Vision: " + "Press e to exit music player." + '\n')
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)
           music.play_music()
           
         
       elif "detect" in a or "find" in a or "detection" in a:
           result = True
           while(result):
               ret,frame = videoCaptureObject.read()
               cv2.imwrite("./input/NewPicture.jpg",frame)
               result = False
           videoCaptureObject.release()
           cv2.destroyAllWindows()
           detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
           ChatLog.config(state=NORMAL)
           ChatLog.insert(END, "Vision: " + "itemas detected are" + '\n')
           ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
           ChatLog.config(state=DISABLED)
           ChatLog.yview(END)
           for eachItem in detection:
               print(eachItem["name"])
               ChatLog.config(state=NORMAL)
               ChatLog.insert(END, "Vision: " + eachItem["name"] + '\n')
               ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
               ChatLog.config(state=DISABLED)
               ChatLog.yview(END)
               SpeakText(eachItem["name"])
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
               SpeakText("Sending message")
               SpeakText("Message sent")
           else:
               SpeakText("receiver not available")
       
        
        
       elif "message" in a or "sms" in a:
           SpeakText("Who is the receiver")
           try:
               with sr.Microphone() as source2:
                   audio2 = r.listen(source2)
                   receive = r.recognize_google(audio2)
                   print(receive)
           except sr.UnknownValueError:
              
               print("message was not clear")
           
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
               
               sms.send_sms(message,phno)
           else:
               SpeakText("receiver not available")
        
           
               
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
        ChatLog.config(state=NORMAL)
        
        ChatLog.insert(END, "Vision: " + "Sorry! I Could not understand you." + '\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
        
def maintext():
    a = EntryBox.get("1.0",'end-1c')
    EntryBox.delete("0.0",END)
    a=a.split(" ")
    print(a)
            
    if "read" in a and "email" in a:
        content=readmail.readmymail()
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: subject: " + str(content[0]) + '\n\n')
        ChatLog.insert(END, "Vision: from: " + str(content[1]) + '\n\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
            
    
    elif "email" in a:
        
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("siddhu.dash@gmail.com", "65477412") 
        SpeakText("Welcome to email services!")
        SpeakText("Please enter the receiver's name")
        
        receive="did not get"
        message="not clear"
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: " + "Please enter the receiver's name" + '\n\n')
        
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END) 
        
        receive= tkinter.simpledialog.askstring(title="Welcome to email widget",prompt="Enter receiver name")
        EntryBox.delete("0.0",END)
        
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + receive + '\n\n')
        
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END) 
    
        
        
        if receive.lower() in emaildb:
            receive=receive.lower()
            emailid=emaildb[receive]
            
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "vision: " + "please enter your message" + '\n\n')
            
            ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)  
            SpeakText("Please enter your message")           
            
            message= tkinter.simpledialog.askstring(title="Welcome to email widget",prompt="Enter your message")
            EntryBox.delete("0.0",END)
            
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + message + '\n\n')
            
            ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)  
            
            SpeakText("Sending")
            s.sendmail("siddhu.dash@gmail.com", emailid, message) 
            s.quit() 
                 
            print("email sent")
            SpeakText("email sent")
        else:
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Vision: " + "Receiver not available" + '\n')
            ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)    
            
    elif "help" in a or "helpdesk" in a:
        helpdesk.helpdesk()
    elif "settings" in a or "adjust" in a or "setting" in a:
        settings.settings()
    elif "weather" in a:
        report=API.weather_api()
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: city: " + report[0] + '\n\n')
        ChatLog.insert(END, "Vision: temperature: " + report[1] + '\n\n')
        ChatLog.insert(END, "Vision: humidity: " + report[2] + '\n\n')
        ChatLog.insert(END, "Vision: pressure: " + report[3] + '\n\n')
        ChatLog.insert(END, "Vision: forecast: " + report[4] + '\n\n')
        
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    elif "app" in a:
        syspgm.openfile()
                      
    elif "news" in a or "new" in a:
        
        results=API.news_api()
        for i in range(len(results)-5):
            
            print(i+1,results[i])
            SpeakText(results[i])
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Vision: " + str(results[i]) + '\n\n')
            ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
    elif "time" in a:
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        SpeakText(current_time)
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: " + str(current_time) + '\n\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    
    elif "date" in a or "day" in a:
    
    
        today = date.today() 
        print("Today date is: ", today)
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: " + str(today) + '\n\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
                           
       
    elif "calculator" in a:        
        
        SpeakText("enter what you want to calculate, example: 3 plus 3")
        my_string= tkinter.simpledialog.askstring(title="calculator widget",prompt="Enter your equation with spaces separating each operand")
        EntryBox.delete("0.0",END)
        
                  
        SpeakText(my_string+" is")
        SpeakText(eval_binary_expr(*(my_string.split())))
        
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: " + str(my_string)+" = "+str(eval_binary_expr(*(my_string.split()))) + '\n\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
         
    elif "song" in a or "music" in a:
        ChatLog.config(state=NORMAL)
        
        ChatLog.insert(END, "Vision: " + "Music player is On!!" + '\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        runfile('C:/Users/ATMSI/AppData/Roaming/SPB_Data/musicgui.py', wdir='C:/Users/ATMSI/AppData/Roaming/SPB_Data')
        
        
        
        
         
    elif "detect" in a or "find" in a or "detection" in a:
        result = True
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("./input/NewPicture.jpg",frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()
        detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
        for eachItem in detection:
            print(eachItem["name"])
            SpeakText(eachItem["name"])
    elif "whatsapp" in a:
        print("inside whatsapp")
        SpeakText("You are using whatsapp messageing services!")
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: " + "Enter receiver name" + '\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
        
        receive= tkinter.simpledialog.askstring(title="Welcome to Whataspp widget",prompt="Enter receiver name")
        EntryBox.delete("0.0",END)
  
        if receive.lower() in whatsappdb:
            receive=receive.lower()
            phno=whatsappdb[receive]
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "Vision: " + "Enter message" + '\n')
            ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            message= tkinter.simpledialog.askstring(title="Welcome to Whataspp widget",prompt="Enter your message")
            EntryBox.delete("0.0",END)
            
            
                   
            whatsapp.whatsappmsg(message,phno)
            SpeakText("Sending message")
            SpeakText("Message sent")
        else:
            ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Vision: " + "Receiver not available" + '\n')
        ChatLog.config(foreground="#442265",font=("Verdana", 12 ))
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
       
        
       
    elif "message" in a or "sms" in a:
        SpeakText("Who is the receiver")
        try:
            with sr.Microphone() as source2:
                audio2 = r.listen(source2)
                receive = r.recognize_google(audio2)
                print(receive)
        except sr.UnknownValueError:
         
            print("message was not clear")
        
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
               
            sms.send_sms(message,phno)
        else:
            SpeakText("receiver not available")
       
           
              
    



#Creating GUI with tkinter
import tkinter
from tkinter import *


        
        
            
        
        
 
    
base = Tk()
base.title("The VISION")
base.geometry("600x500")
base.resizable(width=FALSE, height=FALSE)
text = tkinter.StringVar() 

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=NORMAL)
ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
ChatLog.config(state=DISABLED)
ChatLog.yview(END)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Speak", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= main )
textButton = Button(base, font=("Verdana",12,'bold'), text="command", width="12", height=5,
                    bd=0, bg="#3224fe", activebackground="#3c9d9b",fg='#ffffff',
                    command= maintext )

#Create the box to enter message

EntryBox = Text(base, bd=0, bg="#cccccc",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=580,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=560)
EntryBox.place(x=135, y=401, height=90, width=320)
SendButton.place(x=6, y=401, height=90)
textButton.place(x=460, y=401, height=90)

base.mainloop()
