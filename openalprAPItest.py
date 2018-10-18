#!/usr/bin/python

import requests
import base64
import json


IMAGE_PATH = '0.jpg'
SECRET_KEY = 'sk_19ea418a96a8c2c65a57db15'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=pl&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)


data=r.json()

#print(json.dumps(data, indent=2))

for i in range(0,len(data["results"])):
    
    print("Numer rejestracyjny: ",data['results'][i]['plate'])
    print("Kolor: ",data['results'][i]['vehicle']['color'][0]['name'])
    print("Lata produkcji: ",data['results'][i]['vehicle']['year'][0]['name'])
    print("Model: ",data['results'][i]['vehicle']['make_model'][0]['name'])
    print("Marka: ",data['results'][i]['vehicle']['make'][0]['name'])
    print()

