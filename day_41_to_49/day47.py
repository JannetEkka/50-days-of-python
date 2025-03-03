"""Day 47: Save a JSON 
 
Write a  function called  save_json. 
This function takes a dictionary below as an argument and 
saves it on a file in JSON format. 
 
Write another function called read_json 
that opens the file that you just saved and reads its content. 
names = {'name': 'Carol','sex': 'female','age': 55}"""

import json

def save_json(names):
    with open("names.json", "w") as outfile:
        json.dump(names, outfile, indent = 3)

def read_json():
    with open("names.json", "r") as openfile:
        return json.load(openfile)

names = {'name': 'Carol','sex': 'female','age': 55}

save_json(names)
print(read_json())