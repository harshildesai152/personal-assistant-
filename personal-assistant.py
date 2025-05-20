from click import BaseCommand
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit 
from pywikihow import WikiHow , search_wikihow
from pytube  import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip 
from time import sleep
from keyboard import press
from keyboard import press
from keyboard import press_and_release
import keyboard
import pyjokes
import pyautogui


for i in range (3):
    a=input("enter your password:- ")
    p_w=open("pass.txt" ,"r")
    pws=p_w.read()
    p_w.close()
    if (a==pws):
        print("wlcome sir")
        break

    elif (i==2 and a!=pws):
        exit()

    elif(a!=pws):
        print("try again")

en = pyttsx3.init('sapi5')  # Initialize the speech engine with 'sapi5'
voices = en.getProperty('voices')

en.setProperty('voice', voices[1].id)  # Set the voice 
en.setProperty('rate',250)              #voice speed




def speak(audio):
    print(f"{audio}")
    en.say(audio)  # Engine speaks the provided text
    en.runAndWait()

def me():

    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("i am python. how can i help you")

def tack():  
                       #you can speck
    r = sr.Recognizer()         #you can spack convert to taxt
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Set a gap of 1 second
        audio = r.listen(source)
    
    try:
        print("wait...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
        return query.lower()
    except Exception as e:
        print("Say that again, please.")
        return None

def yt(term):

    results="https //www.youtube/resault?search_query=" +term
    webbrowser.open(results)
    pywhatkit.playonyt(term)

def ytd():

    click(x=1038,y=63)            # value are put code: sleep(2)          kkk=pyautogui.position()       print(kkk)
    value=hotkey('ctrl','c')
    value=pyperclip.paste()

    li=str(value)
    
    def Downlode(link):
      
      try:
        url=YouTube(link)
        video=url.streams.first()
        video.download('D:\\program .all\\python projects\\yt dow')
        speak("video downlode")

      except Exception as e:
            print(e)
            speak("Sorry, there was an error downloading the video.")
    Downlode(li)



def findeapp():
    speak("open")

    keyboard.press_and_release('windows+s') 
    speak("open app")
    sleep(1)
    
    keyboard.write(f"{query}")
    sleep(1)
    keyboard.press('enter')
    sleep(1)
    

   
#os.startfile("D:\\program .all\\python projects\\yt dow")

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com','pass')
    server.sendmail('xyz@gmail.com',to,content)
    server.close()


if __name__ == "__main__": 

    me()
    data=tack()
    if "your name" in data:
        name="my name is peter"
        speak(name)
    
    elif "your age" in data:
        name="my age is 223 year old"
        speak(name)
    
    elif "thanks bro"  in data:
        name="welcome sir" 
        speak(name)
    

        
    while True:                # Add your logic here            
        query = tack()
        if  query:
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=40)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")
                
            elif 'search on google' in query:
                speak("plese search")
                cm=tack()
                webbrowser.open(f"{cm}")

                
            elif 'open stackoverflow' in query:
                webbrowser.open("https://www.stackoverflow.com")

            
            elif 'play music' in query:
                webbrowser.open("spotify")
            
            elif  'time' in query:
                Time =datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {Time}")

            elif 'open vs code' in query:
                path= "C:\\Users\\harsh\\Downloads\\VSCodeUserSetup-x64-1.70.2.exe"
                os.startfile(path)

            elif 'open notepad' in query:
                path1="C:\\Windows\\notepad"
                os.startfile(path1)
           
            elif 'send email to my friend' in query:
                try:
                    speak("say")
                    content=tack()
                    to="abc@gmail.com"
                    sendemail(to,content)
                    speak("email send ")
                except Exception as e:
                    print(e)
                    speak("sorry email is not send")


            elif 'search youtube' in query:
                yt(query)
                
            elif 'download yt video' in query: 
                ytd()
                 
            elif 'music start' in query:
                press('space bar')
            
            elif 'music stop' in query:  
                press('space bar')
            
            elif 'new tab' in query:
                press_and_release('ctrl + t')
                #chrome()
            elif 'close tab' in query:
                press_and_release('ctrl + w')

            elif 'new window' in query:
                press_and_release('ctrl + n')
    
            elif 'history' in query:
                press_and_release('ctrl + h')

            elif 'downloads' in query:
                press_and_release('ctrl + j')
    
            elif 'bookmark' in query:
                press_and_release('ctrl + d')
                press('enter')
            
            elif 'skip' in query:
                press('l') 

            elif 'back' in query:
                press('j')
            
            elif 'mute' in query:
                press('m')

            elif 'full screen'  in query:
                press('f')
            
                        
            elif ' ' in query:
                findeapp() 

            elif 'exit' in query:
                speak("Goodbye!")
                break    

            

            
           
