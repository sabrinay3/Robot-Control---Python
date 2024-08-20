import numpy as np
import time

import pickle #new
from datetime import datetime #new
import math #new

import UdpComms as U

# Create UDP socket to use for sending (and receiving) Use THIS machines IP
#sock = U.UdpComms(udpIP="192.168.10.101", sendIP = "192.168.10.100", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=False) #house
sock = U.UdpComms(udpIP="172.26.52.244", sendIP = "172.26.42.4", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=False) #school
recieved_count = 0

messages = []
timestamps = []

startTime = time.time()
endTime = time.time() + 20
while endTime >= time.time():
    data = sock.ReadReceivedData() # read data
    if data != None: # if NEW data has been received since last ReadReceivedData function call
        sock.SendData(str(recieved_count)) # Send this string to other application
        messages.append(data)
        timestamps.append(time.time()-startTime)
        recieved_count += 1

with open('recordedmessages.pkl', 'wb') as file:
    pickle.dump([messages, timestamps], file)

print(messages)
print(timestamps)