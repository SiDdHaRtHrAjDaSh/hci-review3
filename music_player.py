# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 04:10:28 2020

@author: SIDDHARTH RAJ DASH
"""
import speech_recognition as sr 
import pyttsx3
from pygame import mixer  
import pygame
import keyboard

r = sr.Recognizer() 

def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 

def play_music():
    try:
        with sr.Microphone() as source2:
            SpeakText("what song would you like to hear")
            r.adjust_for_ambient_noise(source2, duration=0.5)
            audio2 = r.listen(source2)
            song_name = r.recognize_google(audio2)
        
    except sr.UnknownValueError:
        SpeakText("message was not clear")
    song_name=song_name.lower()
    print(song_name)
    mixer.init() 
    try:
        mixer.music.load("./songs/"+song_name+".mp3") 
    except pygame.error:
        SpeakText("Song unavailable")
        return
    
    SpeakText("Press P to pause.")
    SpeakText("Press r to Resume.")
    SpeakText("Press e to exit music player.")
    
        
        
    mixer.music.set_volume(0.7) 
    mixer.music.play() 
    while True: 
        
                
        if keyboard.is_pressed('p'):
            mixer.music.pause()      
        if keyboard.is_pressed('r'):
            mixer.music.unpause() 
        if keyboard.is_pressed('e'):
            mixer.music.stop() 
            break