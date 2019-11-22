# import wave
import os
# from playsound import playsound
import speech_recognition as sr
r = sr.Recognizer()

# .wav file causes some errors I could not fix
# colors = wavio.read('../color_sounds.wav')

def response(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say: " + audio)
    
def voice_command():
    colors = sr.AudioFile('../color_sounds.flac')
    with colors as source:
        audio = r.record(source)
    
    try:
        s = r.recognize_google(audio)
        # print(s)
        response(s)
        assistant(s)
    except Exception as e:
        print("Exception: " + str(e))

def assistant(command):
    "if statements for executing commands"
        
    # print
    if 'yellow' in command:
        print("the voice said: " + command)

while True:
   # playsound('color_sounds.mp3')
    voice_command()
     