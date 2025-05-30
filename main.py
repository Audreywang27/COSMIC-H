import random

def alt():
    altitude = random.randint(0,10000)
    print(f"Altitude: {altitude} feet")
    return altitude

def temp():
    temperature = random.randint(-60,100)
    print(f"Temperature: {temperature}*C")
    return temperature

def gps():
    lattitude = random.uniform(20.0,50.0)
    longitude = random.uniform(-180.0,180.0)
    print(f"Lattitude = {lattitude}")
    print(f"Longitude = {longitude}")
    return lattitude,longitude

alt()
temp()
gps()