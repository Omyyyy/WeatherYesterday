from tkinter import *
from tkinter import ttk
import getweather
import datetime


def fahr(celc):
    fahr = celc * 1.8 + 32
    return round(fahr, 2)

def insertdata():
    city = city_entry.get().capitalize()
    country = country_entry.get().capitalize()
    day = int(yesterday[2])
    month = int(yesterday[1])
    year = int(yesterday[0])
    avgtemp = getweather.avgtemp(day, month, year, country, city)
    avgprecip = getweather.avgprecip(day, month, year, country, city)
    mintemp = getweather.mintemp(day, month, year, country, city)
    maxtemp = getweather.maxtemp(day, month, year, country, city)
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

root = Tk()
root.title("WeatherYesterday")
root.geometry("1200x800")

city_entry = Entry(root, width= 60, font=("Arial", 20))
city_entry.focus_set()
city_entry.pack(padx=10, pady=10)

country_entry = Entry(root, width= 60, font=("Arial", 20))
country_entry.focus_set()
country_entry.pack(padx=10, pady=10)

ttk.Button(root, text= "Go" ,width= 30, command=insertdata).pack(pady=20)

root.mainloop()