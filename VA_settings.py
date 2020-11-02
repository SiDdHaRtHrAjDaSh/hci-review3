

import speech_recognition as sr 
import pyttsx3

engine = pyttsx3.init()
def SpeakText(command): 
	
	# Initialize the engine 
	 
	engine.say(command) 
	engine.runAndWait() 
	

r = sr.Recognizer() 
def settings():
    
    SpeakText("Welcome to settings. Here you can controll the volume and speech rate of yoour assistant")
    SpeakText("to adjust Volume say volume")
    SpeakText("to adjust speech rate say rate")
    SpeakText("to exit settings say Done!")
    
    
    
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
                
            if "rate" in a or "speed" in a:
                rate = engine.getProperty('rate')
                rate=rate
                SpeakText("this is Speech rate control current speech rate is "+str(rate))
                SpeakText("Say the new speed in words per minute")
                spd=rate
                try:
                    with sr.Microphone() as source2:
                        audio2 = r.listen(source2)
                        spd = r.recognize_google(audio2)
                        print(spd)
                except sr.UnknownValueError:
                    SpeakText("message was not clear")
                    SpeakText("rate is unchanged")
                try:
                    spd=int(spd)
                    
                except ValueError:
                    spd=rate
                    SpeakText("message was not clear")
                engine.setProperty('rate', spd) 
                SpeakText("speed adjusted")
                
                
            
            elif "volume" in a:
                volume = engine.getProperty('volume')
                
                volume=volume*100
                SpeakText("this is volume control current volume is "+str(volume))
                
                SpeakText("Say the new volume under 100")
                vol=volume/100
                try:
                    with sr.Microphone() as source2:
                        print("speak now")
                        audio2 = r.listen(source2)
                        vol = r.recognize_google(audio2)
                        print(vol)
                except sr.UnknownValueError:
                    SpeakText("message was not clear")
                    SpeakText("rate is unchanged")
                
                try:
                    vol=int(vol)
                    
                except ValueError:
                    vol=volume/100
                    SpeakText("message was not clear")
                    
                if vol>100:
                    vol=100
                engine.setProperty('volume', vol/100) 
                SpeakText("Volume adjusted")
            
            elif "done" in a:
                SpeakText("Settings Applied")
                return
                
                   
            
            
            
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
            
    