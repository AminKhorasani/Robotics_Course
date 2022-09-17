import time
import serial
import numpy as np
from vpython import *

arduino_data = serial.Serial('com8', 115200)
time.sleep(1)

toRad = np.pi/180.0
toDeg = 1/toRad

# Simulate pong game using VPython here

# Def your function here


while True:
    while arduino_data.inWaiting() == 0:
        pass
    data_packet = arduino_data.readline()
    try:
        data_packet = str(data_packet, 'utf-8')
        split_packet = data_packet.split(",")
        roll = float(split_packet[0])*toRad
        pitch = float(split_packet[1])*toRad
        yaw = float(split_packet[2])*toRad
        print(roll*toDeg, pitch*toDeg, yaw*toDeg)
        
        # Change the attributes of your object to syncronize it with real time motions

    except:
        pass