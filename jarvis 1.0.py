import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import cv2
import cvzone
import time


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)



def wishme():
    speak("Welcome back Mr.sridharan.")

    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good morning sir")
    if hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-US')
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"




if __name__ == "__main__":
    is_sleeping = False


    while True:
        query = TakeCommand().lower()
        if query.startswith('jarvis'):
            query = query.replace('jarvis', '').strip()  # Remove 'jarvis' from the query
            
            if is_sleeping and 'wake up' not in query:
                continue  # Continue listening if Jarvis is sleeping
            
            if 'sleep' in query:
                speak("Goodbye, Sir. I am going to sleep.")
                is_sleeping = True
            
            elif 'wake up' in query:
                wishme()
                speak("I am awake now.")
                is_sleeping = False

            if 'time' in query:
                time_()

            elif 'date' in query:
                date_()

            elif 'wikipedia' in query:
                speak("searching.....")
                query = query.replace('wikipedia', '')
                result = wikipedia.summary(query, sentences=3)
                speak('According to wikipedia')
                print(result)
                speak(result)

            elif 'search in firefox' in query:
                speak('What should I search?')
                chromepath = 'C:\Program Files\Mozilla Firefox\firefox.exe %s'
                search = TakeCommand().lower()
                wb.get(chromepath).open_new_tab(search + '.com')

            elif 'search in youtube' in query:
                speak('What to search')
                search_Term = TakeCommand().lower()
                speak("Here we go to YOUTUBE")
                wb.open('https://www.youtube.com/results?search_query=' + search_Term)

            elif 'shutdown' in query:
                speak('Shuting down...')
                break

            elif 'black and white' in query:
                cap = cv2.VideoCapture(0)
                while True:
                    _, frame = cap.read()
                    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('Snap control by Voice', gray_scale)

                    stop_command = TakeCommand().lower()
                    if 'close' in stop_command or 'stop' in stop_command:
                        break

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()

            elif 'sunglass' in query:
                cap = cv2.VideoCapture(0)
                cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                overlay = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)
                while True:
                    _, frame = cap.read()
                    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = cascade.detectMultiScale(gray_scale)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        overlay_resize = cv2.resize(overlay, (w, h))
                        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
                    cv2.imshow('Snap control by Voice', frame)
                    stop_command = TakeCommand().lower()
                    if 'close' in stop_command or 'stop' in stop_command:
                        break
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            
            elif 'star glass' in query:
                cap = cv2.VideoCapture(0)
                cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                overlay = cv2.imread('star.png', cv2.IMREAD_UNCHANGED)
                while True:
                    _, frame = cap.read()
                    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = cascade.detectMultiScale(gray_scale)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        overlay_resize = cv2.resize(overlay, (w, h))
                        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y])
                    cv2.imshow('Snap control by Voice', frame)
                    stop_command = TakeCommand().lower()
                    if 'close' in stop_command or 'stop' in stop_command:
                        break
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()                    
                cv2.destroyAllWindows()
            
            elif 'stop listening' in query:
                speak('for how many second')
                ans = int(TakeCommand)
                

