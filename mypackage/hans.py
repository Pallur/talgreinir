import speech_recognition as sr
import re
import webbrowser

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
        else:
            pass

