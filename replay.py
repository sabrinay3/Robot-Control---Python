import pickle
import numpy as np
import time
import math #new

import UdpComms as U

# Create UDP socket to use for sending (and receiving) Use THIS machines IP
#sock = U.UdpComms(udpIP="192.168.10.101", sendIP = "192.168.10.100", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=False) #house
#sock = U.UdpComms(udpIP="172.26.68.237", sendIP = "172.26.42.4", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=False) #school
recieved_count = 0

def translateRotations(data):
        translated_angles = []
        splitdata = data.split('\t')

        for i in splitdata:
            angle = float(i)
            translated_angle = 3 + (angle / math.pi) * 2
            if translated_angle > 5: 
                translated_angle = 5.00
                translated_angles.append(translated_angle)
            else:
                translated_angles.append(translated_angle)
        return translated_angles
    

with open('recordedmessages.pkl', 'rb') as file:
    pickledata = pickle.load(file)

    messages = pickledata[0]
    timestamps = pickledata[1]

print(messages)

# startTime = time.time()
# endTime = time.time() + 20

for data in messages:
    splitdata = data.split("\n")[3].strip()
    # print(splitdata.strip())
    rotateddata = translateRotations(splitdata)
    thumbdata = rotateddata[0:3]
    indexdata = rotateddata[3:6]
    middledata = rotateddata[6:9]
    ringdata = rotateddata[9:12]
    # print("thumb:")
    # print(thumbdata)
    # print("index:")
    # print(indexdata)
    # print("middle:")
    # print(middledata)
    # print("ring:")
    # print(ringdata)
    print(rotateddata)