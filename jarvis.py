import pyttsx3 #...for voice in device 
import speech_recognition as sr #...to take audio as input
import datetime #...to get date and time as input
import wikipedia
import webbrowser #...to open websites
import os
import smtplib #...to send email

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#...To speak audio...
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#...To greet user...
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morining!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

#...takes microphone input from user and returns string output...
def takeCommand():         
    r = sr.Recognizer()        # Initialize the recognizer

    # Open the microphone for capturing audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')     # Recognize the speech
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

#...Send Email...
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing task based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stckoverflow' in query:
            webbrowser.open("stckoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\songs\\favourite song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%s")
            speak(f"Sir, the time is{strTime}")

        elif 'email to shubham' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "shubham.nagare0777@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send the email")

        elif 'quit' in query:
                exit()





    
