from tkinter import *
import getweather
import datetime

def fahr(celc):
    fahr = celc * 1.8 + 32
    return round(fahr, 2)

def insertdata():
    T = Text(root, state = "disabled", height=1200, width=800, font=("Arial", 20))
    T.pack()
    T.configure(state='normal')
    T.insert(END, f"""
Weather in {city}, {country} yesterday:    
    Average temperature on {day}/{month}/{year}: {avgtemp}°C / {fahr(avgtemp)}°F
    Average precipitation on {day}/{month}/{year}: {avgprecip}mm
    Minimum temperature on {day}/{month}/{year}: {mintemp}°C / {fahr(mintemp)}°F
    Maximum temperature on {day}/{month}/{year}: {maxtemp}°C / {fahr(maxtemp)}°F
""")
    T.configure(state='disabled')


yesterday = str(datetime.date.today() - datetime.timedelta(days=1)).split("-")

country = "Switzerland"
city = "Geneva"
day = int(yesterday[2])
month = int(yesterday[1])
year = int(yesterday[0])
avgtemp = getweather.avgtemp(day, month, year, country, city)
avgprecip = getweather.avgprecip(day, month, year, country, city)
mintemp = getweather.mintemp(day, month, year, country, city)
maxtemp = getweather.maxtemp(day, month, year, country, city)

root = Tk()
root.title("WeatherYesterday")
root.geometry("1200x800")
insertdata()
root.mainloop()