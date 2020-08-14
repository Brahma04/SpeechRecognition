# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 07:48:55 2020

@author: user
"""

import speech_recognition as sr
r= sr.Recognizer()   
with sr.Microphone() as source:
    print('speak Anything:')
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print('you said :{}'.formate(text))      # audio into text part
    except:
        print('sorry could not recognize your voice')
                                                # except is used not identify audio