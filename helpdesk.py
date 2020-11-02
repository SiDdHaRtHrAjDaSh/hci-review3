

import speech_recognition as sr 
import pyttsx3

def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
	

r = sr.Recognizer() 
def helpdesk():
    
    SpeakText("Welcome to the helpdesk! say list to get an idea of the commands available in the program or say a command to know ehat it does")
    SpeakText("to exit helpdesk say Bye!")
    
    while(1):
        
        
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
            if  "list" in a or "lists" in a:
                SpeakText("Hi! the commands available are")
                SpeakText("Email")
                SpeakText("weather")
                SpeakText("date and time")
                SpeakText("messaging services")
                SpeakText("Start apps")
                SpeakText("news")
                SpeakText("Music")
                SpeakText("calculator")
                SpeakText("Object detection")
                
                
    
            elif "email" in a:
                SpeakText("this command sends an email to one of your registered contacts")
    
    
            elif "weather" in a:
                SpeakText("this command tells you the latest weather data of your current city")
            elif "date" in a or "time" in a:
                SpeakText("this command tells you the current date and time")
            elif "news" in a:
                SpeakText("this command gives you the lastest news")
            elif "musicr" in a:
                SpeakText("this command plays your favourait music")
            elif "calculator" in a:
                SpeakText("this command activates the voice calculator")
            elif "detect" in a:
                SpeakText("this command scans your surroundings and tells you what is around")
            elif "messaging" in a:
                SpeakText("this command sends a message via sms or whatsapp based on your request, say whatsaap for a whatsapp message and sms for text message")    
            elif "start apps" in a:
                SpeakText("this command starts and opens applications")   
            elif "bye" in a:
                SpeakText("thank you for using helpdesk!!")
                return
                
                   
            
            
            
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
            SpeakText("Sorry i could not understand you")
    