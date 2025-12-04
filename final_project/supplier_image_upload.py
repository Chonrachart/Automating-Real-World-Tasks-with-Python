#!/usr/bin/env python3

import os
import requests

# set path
picture_path = os.path.join(os.getcwd(), 'feedback') 
list_of_picture = os.listdir(picture_path)

# check path and content in directory
print(f"this is picture path that feedback come form:{picture_path}")
print(f"this is list of picture:{list_of_picture}")

""" try to upload picture that process by changeImage.py
    to URL
"""

URL = "http://34.82.90.146/feedback/"

for picture in list_of_picture:
    if picture.endswith(".jpeg"):
        with open(os.path.join(picture_path, picture), 'rb') as img:
            files = {"file": img}
            response = requests.post(URL, files=files)
            # check response form URL
            if response.status_code == 200:
                print(f"Upload {picture} Successful")
            else:
                print(f"Unable to Upload {picture}")
                print(response.text)
        
        