import base64
import os
import time
import sys
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query






password = "open"  
encode = base64.b64encode(password.encode("utf-8"))

def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    speak('Enter your password for Lock or Unlock your folder:')
    query = takeCommand().lower()
    pw = str(input("Enter your password for Lock or Unlock your folder: "))

    if pw == base64.b64decode(encode).decode("utf-8")  :
    # Change Dir Path where you have Locker Folder
        os.chdir('''C:\\Users\\91989\\OneDrive\\Desktop\\the project one\\THE-PROJECT-ONE-main''')
    # If Locker folder or Recycle bin does not exist then we will be create Locker Folder 
        if not os.path.exists("Locker"):
            if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                os.mkdir("Locker")
            else:
                os.popen('attrib -h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}","Locker")
                sys.exit()
        else:
            os.rename("Locker","Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
            os.popen('attrib +h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
            sys.exit()
        
    else:
        print ("Wrong password!, Please Enter right password")
        time.sleep(5)
        goto(1)
