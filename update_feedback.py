#!/usr/bin/env python3

import os
import requests

# set path
data_path = os.path.join(os.getcwd(), 'feedback') 
list_of_feedback_file = os.listdir(data_path)

# check path and content in directory
print(f"this is data path that feedback come form:{data_path}")
print(f"this is list of files:{list_of_feedback_file}")

""" example of content in feedback structure like 
    title
    name
    date
    feedback

        Good deal for a 2015 RAV4
        Anonymous
        2018-04-17
        Called them to look for a second-hand RAV4 and they are very nice and patience 
        to help me find me a few matches then scheduled an appointmet with me. 
        Came in and they had everything ready for me. I was surprised how professional 
        those sales are and they explained and answered all my questions. Ended up buying 
        the car and been using it for more than a month now. Everything 
        looks good!

"""

feedback_data = []
URL = "http://34.82.90.146/feedback/"

for feedback in list_of_feedback_file:
    with open(os.path.join(data_path, feedback), "r") as f:
        feedback_data.append({"title":f.readline().strip(),
                            "name":f.readline().strip(),
                            "date":f.readline().strip(),
                            "feedback":f.read().strip(),
                            })
        
#check feedback_data
#print(f"this check feedback_data:{feedback_data[0]}")

for feedback in feedback_data:
    response = requests.post(URL, json=feedback)
    # check response form URL
    #response.raise_for_status()
    print(f"Created feedback{response.json()['id']}") # change json file from response to python dict and access key "id"