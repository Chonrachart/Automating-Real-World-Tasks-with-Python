#!/usr/bin/env python3

import os
import requests

# set path
data_path = os.path.join(os.getcwd(), 'feedback') 
list_of_text_file = os.listdir(data_path)

# check path and content in directory
print(f"this is data path that feedback come form:{data_path}")
print(f"this is list of files:{list_of_text_file}")

""" example of content in text structure like 
    name
    weight
    description
    and JSON diretory need image_name

        Mango
        300 lbs
        Mango contains higher levels of vitamin C than ordinary fruits. 
        Eating mango can also reduce cholesterol and triglycerides, and help prevent cardiovascular disease. 
        Due to its high level of vitamins, regular consumption of mango play an important role 
        in improving body function and moisturizing the skin.

"""

fruit_data = []

URL = "http://34.82.90.146/feedback/"

for txt in list_of_text_file:
    image_name_only = os.path.splitext(txt)[0]
    with open(os.path.join(data_path, txt), "r") as f:
        fruit_data.append({"name":f.readline().strip(),
                            "weight":int(f.readline().split()[0]), #convert "300 lbs" to int 300
                            "description":f.read().strip(),
                            "image_name":image_name_only,
                            })
        
#check fruit_data
#print(f"this check fruit_data:{feedback_data[0]}")

for fruit in fruit_data:
    response = requests.post(URL, json=fruit)
    # check response form URL
    if response.status_code == 201:
        print(f"Upload {fruit['name']} Successful")
    else:
        print(f"Unable to Upload {fruit['name']}")
        print(response.text)