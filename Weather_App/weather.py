import requests
from pathlib import Path
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()  # loading enviroment variables

def weather():
    configure()
    City = input("Enter the City for Weather Report:- ")
    valid_City = requests.get(f'https://www.geonames.org/search.html?q={City}&country=')

    if valid_City.status_code == 200:
        api_Key ="d2b822ee93ccdd3a81b6c27d5da1a66a"
        weather_Data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={City}&units-imperial&APPID={os.getenv('api_Key')}")
        weather_Data = weather_Data.json()

        dd_file  = Path("city_Report.txt")
        if not dd_file.is_file():
            f = open("city_Report.txt", "x")  # creating the file, if not there
        
        with open("city_Report.txt", "a+") as f:
            f.write('-----------------------\n')
            f.write("City -> " + City + "\n")
            f.write("Country -> " + str(weather_Data['sys']['country']) + "\n")
            f.write('Weather -> ' + str(weather_Data['weather'][0]['main']) + "\n")
            f.write('Humidity -> ' + str(weather_Data['main']['humidity']) + "\n")
            f.write('Temperature ->' + str(weather_Data['main']['temp']) + "\n")
            f.write("Visibility -> " +str( weather_Data['visibility']) + "\n")
            f.write("Wind Speed-> " + str(weather_Data['wind']['speed']) + "\n")
            f.write('-----------------------\n')
        
        f = open("city_Report.txt", "r")
        print(f.read())
    else:
        print("Valid City is Not entered")
