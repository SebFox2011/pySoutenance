import json, requests
import os,time
from lightSensor import lightSensor

payload = {'idEmetteur': 'idFFFFF', 'typeEvenement': 'ouverture'}

def createEvent():
    print("évenement crée")
    r = requests.post("http://10.23.161.7:5000/event/add", data=payload)

while True:
    value=lightSensor.read_light()
    if (value < 1000):
        createEvent()
        print(value)
        time.sleep(3)
    else:
        time.sleep(1)
        print(value)
    
    

