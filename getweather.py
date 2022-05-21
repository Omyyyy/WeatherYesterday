from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily, Stations

def avgtemp(day, month, year, city = "Vancouver"):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    vancouver = Point(49.2497, -123.1193, 70)

    data = Daily(vancouver, start, end)
    data = data.fetch().values.tolist()

    return data[0][0]

def avgprecip(day, month, year, city = "Vancouver"):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    vancouver = Point(49.2497, -123.1193, 70)

    data = Daily(vancouver, start, end)
    data = data.fetch().values.tolist()

    return data[0][3]

def mintemp(day, month, year, city = "Vancouver"):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    vancouver = Point(49.2497, -123.1193, 70)

    data = Daily(vancouver, start, end)
    data = data.fetch().values.tolist()

    return data[0][1]

def maxtemp(day, month, year, city = "Vancouver"):
    start = datetime(year, month, day)
    end = datetime(year, month, day)

    vancouver = Point(49.2497, -123.1193, 70)

    data = Daily(vancouver, start, end)
    data = data.fetch().values.tolist()

    return data[0][2]