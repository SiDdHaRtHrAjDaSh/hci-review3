# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:21:55 2020

@author: SIDDHARTH RAJ DASH
"""
from instapy_cli import client

username = 'sid.photo.archive' #your username
password = 'Siddhu@12345' #your password 
image = 'instapost.jpg' #here you can put the image directory
text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags #pythondeveloper #webdeveloper'
with client(username, password) as cli:
    cli.upload(image, text)