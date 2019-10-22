import json, requests
import os,time

payload = {'idEmetteur': 'idFFFFF', 'typeEvenement': 'ouverture'}

def createEvent():
    print("évenement crée")
    r = requests.post("http://10.23.161.7:5000/event/add", data=payload)

while True:
    createEvent()
    time.sleep(5)

