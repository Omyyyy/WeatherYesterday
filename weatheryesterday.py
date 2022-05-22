from tkinter import Text, END
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, set_appearance_mode, set_default_color_theme
import getweather
import datetime 
import platform

set_appearance_mode("System")
set_default_color_theme("blue")

def fahr(celc):
    fahr = celc * 1.8 + 32
    return round(fahr, 2)

def insertdata():
    city = city_entry.get().title().strip()
    country = country_entry.get().title().strip()
    day = int(yesterday[2])
    month = int(yesterday[1])
    year = int(yesterday[0])
    avgtemp = getweather.avgtemp(day, month, year, country, city)
    avgprecip = getweather.avgprecip(day, month, year, country, city)
    mintemp = getweather.mintemp(day, month, year, country, city)
    maxtemp = getweather.maxtemp(day, month, year, country, city)
    avgwspd = getweather.avgwspd(day, month, year, country, city)
    maxwspd = getweather.peakwspd(day, month, year, country, city)

    if avgtemp is None or avgprecip is None or mintemp is None or maxtemp is None or avgwspd is None or maxwspd is None:
        T.configure(state='normal')
        T.tag_config('warning', foreground="red")
        T.delete(1.0, END)
        T.insert(END, "\nCity not found", 'warning')

    else:
        T.configure(state='normal')
        T.delete(1.0, END)
        T.insert(END, f"""
 Weather in {city}, {country} yesterday:    

 Average temperature on {day}/{month}/{year}: {avgtemp}°C / {fahr(avgtemp)}°F                 Average precipitation on {day}/{month}/{year}: {avgprecip}mm

 Minimum temperature on {day}/{month}/{year}: {mintemp}°C / {fahr(mintemp)}°F                Maximum temperature on {day}/{month}/{year}: {maxtemp}°C / {fahr(maxtemp)}°F

 Average wind speed on {day}/{month}/{year}: {avgwspd}m/s                                    Maximum wind speed on {day}/{month}/{year}: {maxwspd}m/s
""")

    T.configure(state='disabled')

yesterday = str(datetime.date.today() - datetime.timedelta(days=1)).split("-")
weekago = str(datetime.date.today() - datetime.timedelta(days=7)).split("-")
monthago = str(datetime.date.today() - datetime.timedelta(days=30)).split("-")
yearago = str(datetime.date.today() - datetime.timedelta(days=365)).split("-")

root = CTk()
root.title("WeatherYesterday")
if platform.system() == "Windows":
    root.geometry("1920x800")

else:
    root.geometry("1920x1080")
root.resizable(width=False, height=False)

city_label = CTkLabel(master=root, text="City: ", text_font=("Arial", 20))
country_label = CTkLabel(master=root, text="Country: ", text_font=("Arial", 20))
city_label.place(x=657, y=13)
country_label.place(x=630, y=72)

city_entry = CTkEntry(master=root, width= 350, height= 40, text_font= ("Arial", 20))
city_entry.focus_set()
city_entry.pack(padx=10, pady=10)

country_entry = CTkEntry(master=root, width= 350, height= 40, text_font= ("Arial", 20))
country_entry.focus_set()
country_entry.pack(padx=10, pady=10)

CTkButton(master=root, text= "Go" ,width= 100, height=30, text_font=("Arial", 13), command=insertdata).pack(pady=20)

T = Text(master=root, state = "disabled", height=1200, width=800, font=("Nunito Sans", 22))
T.pack()

root.mainloop()