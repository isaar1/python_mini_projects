print("**WEATHER INFORMATION")

import requests
import json
import pyttsx3

city = input("Enter the name fo the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=d5be157061b04b62ac0110635241304&q={city}"

r = requests.get(url)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

engine = pyttsx3.init()

engine.setProperty('rate', 120)  
engine.setProperty('volume', 1.0)  
engine.setProperty('voice', 'english')

text_to_speak = f"The current weather in {city} is {w} degrees"
engine.say(text_to_speak)
engine.runAndWait()