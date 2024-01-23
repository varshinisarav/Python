import requests
import json 

base_url = "https://api.openweathermap.org/data/2.5/weather?"

city = input("Enter a city to get weather details : ")
print("")

api_key = "a49de69b810181cc6659a996563a51dc"

url= base_url + "q=" + city + "&appid=" + api_key
response = requests.get(url)

if response.status_code == 200:
   
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   report = data['weather']
   print("Current Weather Condition in ",city,".....")
   print("")
   print("Temperature in (kelvin): ",temperature)
   print("Humidity in percent(%): ",humidity)
   print("Pressure : ",pressure)
   print(f"Weather Report: {report[0]['description']}")
else:
   print("Error: Unable to get weather conditions")