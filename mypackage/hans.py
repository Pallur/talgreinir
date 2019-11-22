import speech_recognition as sr
import re
import webbrowser
import logging
# import urllib2

def voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something..")
        # logging.info("Say something..")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noice(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command + "\n")
    except sr.UnknownValueError:
        print("...")
        command = voice_command();
    return command

def hans_response(audio):
    print(audio)
    """
    for line in audio.splitlines():
        os.system("say " + audio)
    """

def assistant(command):
    "if statements for executing commands"
    print("you said :" + command)
    #open website
    if 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            hans_response("The website has been opened")
        else:
            pass
    
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        hans_response('Current time is %d hours and %d minutes' %(now.hour), now.minute)
        
"""
while True:
    assistant(voice_command())
"""
