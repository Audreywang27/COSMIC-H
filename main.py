import time
import random
import csv
import datetime
import pytz

height = 0 #Altitude in feet
counter = 0
countUp = 1

while True:
    if height > 13:
        countUp = 0

    if height <= 0 and counter >  1:
        break

    if height < 10:
        counter = counter + 1

    if countUp == 1 and height <=20:
        height = height + 1
    elif countUp == 0:
        height = height - 1
    
    print(height)
    #Simulates sensor data
    def alt():
        altitude = random.randint(0,10000)
        #print(f"Altitude: {altitude} feet")
        return altitude

    def temp():
        temperature = random.randint(-60,100)
        #print(f"Temperature: {temperature}*C")
        return temperature

    def latt():
        lattitude = random.uniform(20.05,50.0)
        #print(f"Lattitude = {lattitude}")
        return lattitude

    def long():
        longitude = random.uniform(-180.0,180.0)
        #print(f"Longitude = {longitude}")
        return longitude

    def timeStamp():
        dt_utcnow = datetime.datetime.now(tz = pytz.UTC)
        dt_est = dt_utcnow.astimezone(pytz.timezone("US/Eastern"))
        #print(f"Time Stamp: {dt_est}")
        return dt_est

    alt()
    temp()
    latt()
    long()
    timeStamp()


    #Simulates Image Data

    #Stimulates storing the data to a CSV file
    #Header = Altitude, Temperature, Coordinates(tuple)
    dataSet = [
        {"Time Stamp": timeStamp(), "Altitude" : alt(), "Temperature" : temp(), "Lattitude" : latt(), "Longitude" : long()}
    ]

    with open("data.csv", mode = "a", newline = "") as csvfile:
        fieldnames = ["Time Stamp", "Altitude", "Temperature", "Lattitude", "Longitude"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(dataSet)

    print("hello")
    time.sleep(1)





