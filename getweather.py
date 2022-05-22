from datetime import datetime
from meteostat import Point, Daily
from geopy.geocoders import Nominatim
import warnings

warnings.filterwarnings("ignore")

geolocator = Nominatim(user_agent="weatheryesterday")

def avgtemp(day, month, year, country, city):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    loc = geolocator.geocode(city+','+ country)

    if loc is None:
        return

    citypoint = Point(loc.latitude, loc.longitude)

    data = Daily(citypoint, start, end)
    data = data.fetch().values.tolist()

    return data[0][0]

def avgprecip(day, month, year, country, city):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    loc = geolocator.geocode(city+','+ country)

    if loc is None:
        return 

    citypoint = Point(loc.latitude, loc.longitude)

    data = Daily(citypoint, start, end)
    data = data.fetch().values.tolist()

    return data[0][3]

def mintemp(day, month, year, country, city):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    loc = geolocator.geocode(city+','+ country)

    if loc is None:
        return 

    citypoint = Point(loc.latitude, loc.longitude)

    data = Daily(citypoint, start, end)
    data = data.fetch().values.tolist()

    return data[0][1]

def maxtemp(day, month, year, country, city):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    loc = geolocator.geocode(city+','+ country)

    if loc is None:
        return

    citypoint = Point(loc.latitude, loc.longitude)

    data = Daily(citypoint, start, end)
    data = data.fetch().values.tolist()

    return data[0][2]

def avgwspd(day, month, year, country, city):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    loc = geolocator.geocode(city+','+ country)

    if loc is None:
        return

    citypoint = Point(loc.latitude, loc.longitude)

    data = Daily(citypoint, start, end)
    data = data.fetch().values.tolist()

    return data[0][6]

def peakwspd(day, month, year, country, city):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    loc = geolocator.geocode(city+','+ country)

    if loc is None:
        return

    citypoint = Point(loc.latitude, loc.longitude)

    data = Daily(citypoint, start, end)
    data = data.fetch().values.tolist()

    return data[0][7]