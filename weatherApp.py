import requests
import json
import pyttsx3


engine = pyttsx3.init()

api_key = '30d4741c779ba94c470ca1f63045390a'

city=input("Enter city :- ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"

r= requests.get(url)
with_dic = json.loads(r.text)
info = input("Enter what kind of information you would like to see:- ")

def check():
    found = 'Please try again giving a valid input'
    for word in info.split():
        if 'temprature' in word:
            print(f"The temperature in {city} is:- ")
            found = with_dic['main']['temp']
            engine.say(f"The temperature in {city} is {found}°")
            engine.runAndWait()
            break

        elif 'pressure' in word:
            print(f"The pressure in {city} is:- ")
            found = with_dic['main']['pressure']
            engine.say(f"The pressure in {city} is {found}")
            engine.runAndWait()
            break

        elif 'humidity' in word:
            print(f"The humidity in {city} is:- ")
            found = with_dic['main']['humidity']
            engine.say(f"The humidity in {city} is {found}")
            engine.runAndWait()
            break

        elif 'speed' in word:
            print(f"The wind speed in {city} is:- ")
            found = with_dic['wind']['speed']
            engine.say(f"The wind speed in {city} is {found}")
            engine.runAndWait()
            break

        elif 'everything' in word:
            print(f"The weather data of {city} is:- ")
            found = with_dic
            engine.say(f"The weather data of {city} is give below")
            engine.runAndWait()
            break

        elif 'coordinates' in word:
            print(f"The wind coordinates in {city} is:- ")
            found = with_dic['coord']
            engine.say(f"The coordinates in {city} is {found}")
            engine.runAndWait()
            break

        elif 'overall' in word:
            print(f"The overall weather in {city} is:- ")
            found = with_dic['weather'][0]['main']
            engine.say(f"The overall weather in  {city} is {found}")
            engine.runAndWait()
            break

        elif 'maximum' in word:
            print(f"The maximum temprature that reached in {city} is:- ")
            found = with_dic['main']['temp_max']
            engine.say(f"The maximum temprature that reached in {city} is {found}°")
            engine.runAndWait()
            break

        elif 'minimum' in word:
            print(f"The minimum temprature that reached in {city} is:- ")
            found = with_dic['main']['temp_min']
            engine.say(f"The minimum temprature that reached in {city} is {found}°")
            engine.runAndWait()
            break
    return found
print(check())
