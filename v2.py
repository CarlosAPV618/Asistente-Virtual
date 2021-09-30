# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:26:14 2021

@author: CarlosAPV618
"""
import speech_recognition as sr
import subprocess as sub
import pyautogui as robot
import pyttsx3 as voz
import time

voice = voz.init()
voice.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
voice.setProperty('rate', 130)

def say(text):
    voice.say(text)
    voice.runAndWait()
    
def buscar(pos,click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)
    
def interpretar(comando_de_audio):
    comando_de_audio = comando_de_audio.split(' ')

    if 'YouTube' in comando_de_audio:
        for i in ['Busca','busca','Buscar','buscar']:
            if i in comando_de_audio:
                sub.call('start brave.exe youtube.com', shell=True)
                comando_de_audio.pop(comando_de_audio.index(i))
                comando_de_audio.pop(comando_de_audio.index('en'))
                comando_de_audio.pop(comando_de_audio.index('YouTube'))
                srch=' '.join(comando_de_audio)
                time.sleep(2)
                buscar((321,101),3)
                robot.typewrite(srch)
                robot.typewrite(' ')
                robot.hotkey('enter')
                say(f'Buscando {srch} en YouTube')
        sub.call('start brave.exe youtube.com', shell=True)
        say('Abriendo Youtube')
    elif 'noticias' in comando_de_audio:
        sub.call('start brave.exe mundo.sputniknews.com', shell=True)
        say('Abriendo Sputnik news')
    elif 'notas' in comando_de_audio:
        sub.call('start notepad.exe', shell=True)
        say('Estoy lista para escribir tu texto')
        r = sr.Recognizer()

        listen=1
        
        while listen==1:
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                comando = r.recognize_google(audio, language='es-MX')
                robot.write(comando)
                        
                if 'fin' in comando:
                    listen=0
                        
            except sr.UnknownValueError:
                print("No te pude entender")
            except sr.RequestError as e:
                print("No pude obtener respuesta del servicio de Google Speech Recognition; {0}".format(e))

    
def asistente():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando")
        audio = r.listen(source)
    
    try:
        # Si se entendió el audio
        comando = r.recognize_google(audio, language='es-MX')
        print("Creo que dijiste "+'"'+comando+'"')
        interpretar(comando) # lo que se debe hacer con el comando de audio
    
    except sr.UnknownValueError:
        # si no se entendió
        print("No te pude entender")
    except sr.RequestError as e:
        # si no se tiene conexión a internet o al servicio de google
        print("No pude obtener respuesta del servicio de Google Speech Recognition; {0}".format(e))
