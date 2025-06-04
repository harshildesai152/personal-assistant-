import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
import threading
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
import os
import smtplib
import pywhatkit
from pytube import YouTube
import pyautogui
import pyperclip
from time import sleep
import keyboard

# Text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

# Modern GUI Setup
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("600x400")
window.resizable(False, False)
window.configure(bg="#f2f2f2")

style = ttk.Style()
style.configure('TButton',
                font=('Helvetica', 14),
                padding=10,
                background='#0078D7',
                foreground='black')  
style.map('TButton',
          background=[('active', '#005A9E')],
          foreground=[('active', 'black')])


title_label = tk.Label(window, text="🎙️  Voice Assistant", font=("Helvetica", 24, 'bold'), bg="#f2f2f2", fg="#333")
title_label.pack(pady=20)

gui_text = tk.StringVar()
output_frame = tk.Frame(window, bg="#ffffff", bd=2, relief='groove')
output_frame.pack(pady=10, padx=40, fill='both', expand=True)

output_label = tk.Label(output_frame, textvariable=gui_text, wraplength=500,
                        font=("Helvetica", 14), bg="#ffffff", fg="#222", justify='left')
output_label.pack(padx=20, pady=20)

# Password Prompt
password_verified = False
for _ in range(3):
    user_input = simpledialog.askstring("Password Required", "Enter your password:", show='*')
    if user_input is None:
        window.destroy()
        exit()

    try:
        with open("pass.txt", "r") as p_w:
            pws = p_w.read().strip()
        if user_input == pws:
            messagebox.showinfo("Access Granted", "Welcome Sir")
            password_verified = True
            break
        else:
            messagebox.showwarning("Access Denied", "Incorrect password. Try again.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Password file not found.")
        window.destroy()
        exit()

if not password_verified:
    window.destroy()
    exit()

def speak(text):
    gui_text.set(text)
    window.update()
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Python. How can I help you?")

def listen_command():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            gui_text.set("🎧 Listening...")
            window.update()
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)
    except OSError:
        gui_text.set("No microphone detected.")
        return ""

    try:
        gui_text.set("🔍 Recognizing...")
        window.update()
        query = recognizer.recognize_google(audio, language='en-in')
        gui_text.set(f"🗣️ You said: {query}")
        return query.lower()
    except:
        gui_text.set("⚠️ Sorry, please say that again.")
        return ""

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('xyz@gmail.com', 'password')
    server.sendmail('xyz@gmail.com', to, content)
    server.quit()

def download_youtube_video():
    pyautogui.click(x=1038, y=63)
    sleep(2)
    keyboard.press_and_release('ctrl+c')
    sleep(1)
    link = pyperclip.paste()
    try:
        yt = YouTube(link)
        video = yt.streams.first()
        video.download('D:\\Downloads')
        speak("Video downloaded successfully.")
    except Exception as e:
        speak("Failed to download video.")

def run_assistant():
    greet_user()
    while True:
        query = listen_command()
        if not query:
            continue

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("open youtube successfully")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'search on google' in query:
            speak("What should I search?")
            cm = listen_command()
            webbrowser.open(f"https://www.google.com/search?q={cm}")

        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com")

        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {Time}")

        elif 'open notepad' in query:
            os.startfile("C:\\Windows\\System32\\notepad.exe")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = listen_command()
                to = "abc@gmail.com"
                send_email(to, content)
                speak("Email has been sent.")
            except Exception as e:
                speak("Sorry, I was not able to send the email.")

        elif 'search youtube' in query:
            term = query.replace('search youtube', '')
            pywhatkit.playonyt(term)

        elif 'download youtube video' in query:
            download_youtube_video()
        
        elif 'music start' in query:
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

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

        else:
            speak("I did not understand. Can you please repeat?")

def start_thread():
    t = threading.Thread(target=run_assistant)
    t.start()

start_button = ttk.Button(window, text="🚀 Start Assistant", command=start_thread)
start_button.pack(pady=20)

# Start the GUI loop
window.mainloop()
