
import tkinter as tk
import openai
import speech_recognition as sr
import os
import threading
import pyttsx3
import mygui
from dotenv import load_dotenv
from datetime import datetime
import pvporcupine
import pyaudio
import struct
import time

USER="sir"

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

# Load Environment variables
load_dotenv()

# Load your OpenAI API key
openai.api_key = os.getenv('OPEN_AI_KEY')


# Set up the speech recognition
def recognize_speech():
    
    r = sr.Recognizer()

    with sr.Microphone(device_index=28) as source:
        print("Listening...")
        audio = r.listen(source)
        while[True]:
            try:
                speech_text = r.recognize_google(audio)
                print("You said: " + speech_text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                



            return speech_text




def text_to_speech(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

    
def continuous_face():
    while True:  # Keep the animation running continuously
        mygui.face()
    
def start_animation():
    mygui.pygame.init()
    mygui.display()
    animation_thread = threading.Thread(target=continuous_face)
    animation_thread.start()
def main_loop():


    mygui.pygame.init()
    mygui.display()
    
    # Start the animation in a new thread as soon as the window opens
    threading.Thread(target=continuous_face).start()
    running = True
    while running:
        for event in mygui.pygame.event.get():
            if event.type == mygui.pygame.QUIT:
                running = False
        
        # Listen for speech and check if the phrase "hello" was said

        start_speech_recognition()
        
            

        mygui.pygame.display.flip()

    mygui.pygame.quit()
    

def send_to_chatGPT(messages, model='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message= response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message
def start_session():
    messages=[{"role": "user", "content":"Please act like Jarvis from Iron Man"}]
    while[True]:
        text = recognize_speech()
        if (text=="stop"):
            mygui.pygame.quit()
            exit()
        
            
    
        else:
            messages.append({"role": "user","content":text})
            response=send_to_chatGPT(messages)

        
        
        text_to_speech(response)
        print (response)

def start_speech_recognition():
    porcupine = None
    pa = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(keywords=["jarvis","computer"])
        pa = pyaudio.PyAudio()
        audio_stream= pa.open(rate= porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm= struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hotword Detected...", end="")
                start_session()
                time.sleep[1]
                print("J.A.R.V.I.S Awaiting your call"+ USER)
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()


    

main_loop()

