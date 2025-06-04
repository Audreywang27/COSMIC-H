import time
import threading
import random
import csv
import datetime
import pytz

#Simulates sensor data
#-----------------------------------------------------------------------------------------------
#The code generated below is by Chat GPT, simulating a very random altitude increase/decrease 

current_altitude = 0.0

def simulate_altitude():
    global current_altitude
    rising = True

    while True:
        if rising:
            # Simulate slow rise with small randomness
            current_altitude += random.uniform(0.5, 1.5)
            if current_altitude > 30000:  # simulate max altitude (30,000 ft)
                rising = False
        else:
            # Simulate slow descent
            current_altitude -= random.uniform(0.5, 1.5)
            if current_altitude < 0:
                current_altitude = 0
                rising = True  # loop back for fun

        #print(f"Simulated Altitude: {round(current_altitude, 2)} ft")
        time.sleep(0.5)  # Adjust speed of simulation
# Returns the latest altitude (used by logger)
def get_altitude():
    return round(current_altitude, 2)
#-----------------------------------------------------------------------------------------
'''
def altcalc():
    global alt_history

    while len(alt_history) == 0:
        time.sleep(0.1)

    maxAlt = alt_history[0]
    while True:
        for i in range(0, len(alt_history)):
            if maxAlt < alt_history[i]:
                maxAlt = alt_history[i]
            elif maxAlt > alt_history[i]:
                print(f"Max reached at {maxAlt}")
                return

'''
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

def humid():
    humiditygenerator = random.uniform(0,100) # going to get rid of this eventually
    #print(f"The humidity is {humiditygenerator}%")
    return humiditygenerator


#Stimulates storing the data to a CSV file
def logger():

    while True:
        dataSet = [
            {"Time Stamp": timeStamp(), "Altitude" : get_altitude(), "Temperature" : temp(), "Humidity" : humid(), "Lattitude" : latt(), "Longitude" : long()}
        ]

        with open("data.csv", mode = "a", newline = "") as csvfile:
            fieldnames = ["Time Stamp", "Altitude", "Temperature", "Humidity", "Lattitude", "Longitude"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows(dataSet)

        time.sleep(1)


#Threading

t1 = threading.Thread(target = simulate_altitude)
t2 = threading.Thread(target = logger)

t1.start()
t2.start()

t1.join()
t2.join()




