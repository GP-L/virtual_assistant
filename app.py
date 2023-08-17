import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recogniziong")
        query = r.recognize_google(audio).lower()
        print(query)
        return query
    except Exception as e:
        print(e)
        print("Sorry, I did not understand that. Say that again please.")
        speak("Sorry, I did not understand that. Say that again please.")


def hello():
    print("Hello, I am your desktop assistant. Tell me how I can help you today.")
    speak("Hello, I am your desktop assistant. Tell me how I can help you today.")


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print("The day is ", day_of_the_week)
        speak("The day is" + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is" + hour + "hours and" + min + "minutes")


def takeQuery():
    hello()

    while True:
        query = takeCommand()
        if "open jw" in query:
            print("Opening JW.org.")
            speak("Opening JW.org.")
            webbrowser.open("https://www.jw.org")
            continue
        elif "open google" in query:
            print("Opening Google.")
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
            continue
        elif "which day is it" in query:
            tellDay()
            continue
        elif "tell me the time" in query:
            tellTime()
            continue
        elif "from wikipedia" in query:
            print("Checking the wikipedia.")
            speak("Checking the wikipedia.")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query)
                print("According to wikipedia, ", result)
                speak("According to wikipedia," + result)
            except Exception:
                speak(
                    "Sorry, I could not find enough information on wikipedia about that"
                )
                print(
                    "Sorry, I could not find enough information on wikipedia about that"
                )
            continue
        elif "tell me your name" in query:
            print("I am Nicco. Your desktop Assistant.")
            speak("I am Nicco. Your desktop Assistant.")
            continue
        elif "bye" in query:
            print("Bye!")
            speak("Bye!")
            exit()


if __name__ == "__main__":
    takeQuery()
