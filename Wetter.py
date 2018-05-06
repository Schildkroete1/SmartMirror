from forecastiopy import *
import os

api_key = "" # bitte ausfuellen
lat = 
lon = 

forecast = ForecastIO.ForecastIO(api_key,
                                units=ForecastIO.ForecastIO.UNITS_SI,
                                                                lang=ForecastIO.ForecastIO.LANG_GERMAN,
                                                                latitude=lat, longitude=lon)
daily = FIODaily.FIODaily(forecast)
currently = FIOCurrently.FIOCurrently(forecast)
print("Wetter aktualisiert")

with open("RAM/Vorhersage.txt", "w") as out:
    out.write("Aktuell: " + currently.summary + "\nVorhersage: " + daily.summary)
    out.close()
with open("RAM/Temperatur.txt", "w") as out:
    out.write(" " + str(FIOCurrently.FIOCurrently(forecast).temperature) + "\xb0C")
    out.close()

os.system("touch RAM/refresh")
