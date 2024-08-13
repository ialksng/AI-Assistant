import text2speech
import speech2text
import datetime
import webbrowser
import weather
import camera
import settings


def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text2speech.text2speech("My name is AlphaBot, your AI Assistant")
        return "My name is AlphaBot, your AI Assistant"
    elif "hello" in user_data or "hi" in user_data:
        text2speech.text2speech("Hi, How can I help you?")
        return "Hi, How can I help you?"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + " Hour :", (str)(current_time.minute) + "Minute" 
        text2speech.text2speech(Time)
        return Time
    elif "shutdown" in user_data:
        text2speech.text2speech("Ok, shutting down!")
        return "Ok, shutting down!"
    elif "play music" in user_data:
        webbrowser.open("https://music.youtube.com/")
        text2speech.text2speech("Enjoy your music on Youtube Music")
        return "Enjoy your music on Youtube Music"
    elif "youTube" in user_data:
        webbrowser.open("https://youtube.com/")
        text2speech.text2speech("Opened Youtube for you")
        return "Opened Youtube for you"
    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        text2speech.text2speech("Opened Google for you")
        return "Opened Google for you"
    elif "camera" in user_data:
        c = camera.camera()
        text2speech.text2speech(c)
        return c
    elif "weather" in user_data:
        r = weather.weather()
        text2speech.text2speech(r)
        return r
    elif "settings" in user_data:
        s = settings.settings()
        text2speech.text2speech(s)
        return s
    else:
        text2speech.text2speech("Sorry, I can't assist you in that!")
        return "Sorry, I can't assist you in that!"

