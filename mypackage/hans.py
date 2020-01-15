import speech_recognition as sr
import re
import webbrowser
import pyaudio

# * command to recognize the speech using a microphone
def voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command + "\n")
    except sr.UnknownValueError:
        print("...")
        command = voice_command();
    return command

def mic_list():
    m_list = sr.Microphone.list_microphone_names()
    return m_list

def assistant(command):
    # * command to open a website
    if 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
        else:
            pass

