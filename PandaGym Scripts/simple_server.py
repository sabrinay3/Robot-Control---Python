import numpy as np
import time
import pickle #new
from datetime import datetime #new
import math

import UdpComms as U

# Create UDP socket to use for sending (and receiving) Use THIS machines IP
#sock = U.UdpComms(udpIP="192.168.10.101", sendIP = "192.168.10.100", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=False) #house
sock = U.UdpComms(udpIP="172.26.68.237", sendIP = "172.26.42.4", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=False) #school
recieved_count = 0

while True:
    sock.SendData(str(recieved_count)) # Send this string to other application
    time.sleep(0.1)
    hand_positions = [] #new

    def add_timestamp(data):
        timestamp = datetime.now().isoformat()
        print('timestamp: ' + timestamp + 'data: ' + data)

    def translateRotations(data):
        handdata = 3 + (data/math.pi) * 2
        data = handdata
    
    data = sock.ReadReceivedData() # read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        hand_positions = data.split("\n")[4]
        time_hand_pos = add_timestamp(hand_positions)
        file_path = 'hand_positions.pkl'

        with open(file_path, 'wb') as file:
            pickle.dump(time_hand_pos, file)
        print(hand_positions) 
        recieved_count += 1
        