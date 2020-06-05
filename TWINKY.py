## T.W.I.N.K.I.E Virtual Assistance

"""MODULES"""
import subprocess
import sys

try:
    from gtts import gTTS
    import speech_recognition as sr     # uses pyaudio itself
    import random
    import wikipedia
    import datetime     # For Time
    import time     # For sleep
    import os   # For clear or cls Terminal
    import calendar 
    import warnings     # For Ignoring Warnings
    import pygame   # For Playing Audio
    import requests     # For Url Requests

except ImportError:
    ModLst = ["gTTS", "SpeechRecognition", "wikipedia", "PyAudio"]

    for item in ModLst:
        subprocess.check_call([sys.executable, "-m", "pip3", "install", item])
finally:
    from gtts import gTTS
    import speech_recognition as sr     # uses pyaudio itself
    import random
    import wikipedia
    import datetime     # For Time
    import time     # For sleep
    import os   # For clear or cls Terminal
    import calendar 
    import warnings     # For Ignoring Warnings
    import pygame   # For Playing Audio
    import requests     # For Url Requests
    
    
# For Clearing Terminal
clear = lambda: os.system('clear' or 'cls')

# Ignore any warnings
warnings.filterwarnings("ignore")

# Audio Recording
def AudioIn():
    r = sr.Recognizer()     # For Recognoizer Object
    
    # Opening Microphone using sr module
    with sr.Microphone() as source:
        clear()
        print("Speak Now...\nSuggestion- 'What can you do?'\n")
        r.pause_threshold = 1   # For ignoring 1sec speak gap
        audio = r.listen(source)

    # Using Google Speech Recognizer

    # For Errors
    try:
        print("Recognizing...\n")
        cmd = r.recognize_google(audio)

        print(f"You Said: {cmd}")

    except sr.UnknownValueError:    # Value Error
        print("Didn't get you")

    except sr.RequestError as e:    # Server Error
        print("Error from Google Speech Recognition server"+ e)

    return cmd

# Responce from Assistant


def VAresponse(text):

    # Text to Speech Converting

    # Using gTTS module
    #> Speech is perfect and accuracy is more but response rate is dependent
    
    obj1 = gTTS(text = text, lang = 'en', slow = False)

    # Saving The Audio
    obj1.save('VAresponse.mp3')

    # Playing Audio
    print(text)
    pygame.mixer.pre_init(22050,-16, 2, 1024)
    pygame.init()
    pygame.mixer.music.load("VAresponse.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.pre_init(22050,-16, 2, 1024)




    '''
    # Using pyttsx3 module
    #> the voice is imperfect but response rate is good
        # Installing
    # pip3 install pyttsx3
    # sudo apt-get install espeak
    
    import pyttsx3
    

    engine = pyttsx3.init()
 
    engine.setProperty('rate', 155)    # setting speech speed rate

    print(text)
    
    engine.say(text)
    engine.runAndWait()
    '''

    '''
    # Using Festival for Speech
    #> Voice is imperfect and speed is high. Response rate is average
    print(text)
    os.system(f"echo {text} |festival --tts")
    '''
    

    
    
# Wake-up words
def WakeVA(text):
    WakeWords = ["hey buddy", "buddy", "ok twinkie", "hey twinky", "twinky", "twinkie"]

    # Lowering Text
    text = text.lower()

    # Checking for wake-up calls
    for items in WakeWords:
        if items in text:
            return True     # If Word Found

    return False    # If Word Not Found

# Greetings
def WishMe():
    Time = int(datetime.datetime.now().hour)
    if Time >= 0 and Time < 12:
        VAresponse("Good Morning Sir. Twinkie is here for you")
    elif Time >= 12 and Time < 18:
        VAresponse("Good Afternoon Sir. Twinkie is here for you")
    else:
        VAresponse("Good Evening Sir. Twinkie is here for you")
    
# Exit Words
def ExitVA(text):
    ExitWords = ['exit', 'close', 'goodbye', 'bye']
    for item in ExitWords:
        if item in text:
            return True
    return False

# Todays Date
def getDate():
    
    today = datetime.datetime.today()
      
    day = calendar.day_name[today.weekday()]
    month = calendar.month_name[today.month]

    year = today.year
    date = today.day

    if date == 1:
        date = str(date) + "st"
    elif date == 2 or int(date)%10 == 2:
        date = str(date) + "nd"
    elif date == 3 or int(date)%10 == 3:
        date = str(date) + "rd"
    else:
        date = str(date) + "th"

    return f'Today is {day} {date} {month}, {year}'

# Created by - Vaibhaw Mishra
def Creator(text):

    CreatorTemp = ['creator', 'created', 'made', 'devloped', 'born']

    for item in CreatorTemp:
        
        if item in text:
            return True
        
    return False

# Current Weather
def Weather():
    VAresponse("Please tell me your city name Sir")

    city = AudioIn()

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e72605818bd664fc9eec2311e96c728e"
    #Note: Please don't use my api id without my permission
         # You are only allowed to use it only through this project
    # You can get your free api for weather from: openweathermap

    res = requests.get(url)

    data = res.json()

    temp = data['main']['temp']

    weather = data['weather'][0]['description']

    VAresponse(f'''Todays Weather condition is: {weather}
And Temperature is {int(temp-273.15)}°C''')

# Current Mood
def Mood(text):
    import itertools
    
    sad = ["not", "unhappy", "sad", "awful"]
    happy = ["happy", "good", "great", "fine", "fantastic"]

    for (item1, item2) in itertools.zip_longest(sad, happy):
        if item1 in text:
            return False
        
        elif item2 in text:
            return True
        
    return 0

# VA's functionalities
def CanDo():
    text = '''I am currently available with these functionalities.
1. Current Time
2. Current Date
3. Search in Wikipedia
4. Tell Current Weather Conditions
5. Response to your current mood(Command- How Are you?)
6. To exit just say Goodbye
Any Contribution will be helpfull.
You can contact my developer through these:'''
    VAresponse(text)
    print('''Devloper Contact: vaibhavmishra658@gmail.com
Instagram: @itsvaibhavmishra
Twitter: @imvaibhavmishra
GitHub: @itsvaibhavmishra''')
    time.sleep(4)
    


if __name__ == '__main__':
    clear()

    # Wake-up experimental
    '''
    if WakeVA(query) is True:
    '''

    WishMe()
    
    
    while True:
        welcome = ["At your service sir", "what can I do for you sir", "I am here for you", "Your command Sir"]
        welcome = random.choice(welcome)
        VAresponse(welcome)
        query = AudioIn().lower()
        
        if 'wikipedia' in query:
            VAresponse("Searching Wikipedia...")
            query = query.replace('wikipedia', "")  # removing wikipedia word
            results = "According to wikipedia:\n"+wikipedia.summary(query, sentences = 2)
            
            VAresponse(results)

        elif 'do' in query:
            CanDo()

        elif Creator(query) is True:
            print('''Devloper Contact: vaibhavmishra658@gmail.com
Instagram: @itsvaibhavmishra
Twitter: @imvaibhavmishra
GitHub: @itsvaibhavmishra''')
            VAresponse('I was created by Vaibhaw Mishra on 3rd June, 2020 as a mini project')

        elif 'how are you' in query:
            VAresponse("I am good Sir. What about you?")
            respond = AudioIn().lower()

            if Mood(respond) is False:
                VAresponse("Sorry to here that Sir.")
            elif Mood(respond) is True:
                VAresponse("Glad to know that Sir.")
            elif Mood(respond) == 0:
                VAresponse("I dont understand sir")
            

        elif 'time' in query:
            now = datetime.datetime.now()
            time = "Time is " + now.strftime("%I:%M %p")
            VAresponse(time)

        elif 'date' in query:
            date = getDate()
            VAresponse(date)

        elif 'weather' in query:
            Weather()
            
        elif ExitVA(query) is True:
            break
        else:
            continue
    VAresponse("GoodBye Sir")
        
