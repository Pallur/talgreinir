import speech_recognition as sr
import re
import webbrowser
import pyaudio
import logging

# * command to recognize the speech using a microphone
def voice_command():
    # ? mlist = sr.Microphone.list_microphone_names()
    # ? print("microphones are: ", mlist)

    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print(sr.Microphone())
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

# * display available microphones (?)
def mic_list():
    mlist = sr.Microphone.list_microphone_names()

    return mlist

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

