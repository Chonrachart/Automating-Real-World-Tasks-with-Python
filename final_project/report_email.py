#! /usr/bin/env python3

import os 
import datetime
from emails import generate_email, send_email
from reports import generate_report  


#set date
date = datetime.date.today().strftime("%B %d, %Y")

# set path
data_path = os.path.join(os.getcwd(), 'feedback') 
list_of_text_file = os.listdir(data_path)
save_report_path = "/tmp/processed.pdf"

# check path and content in directory
print(f"this is data path that feedback come form:{data_path}")
print(f"this is list of files:{list_of_text_file}")


# create data of fruits
fruits_data = []

for txt in list_of_text_file:
    image_name_only = os.path.splitext(txt)[0]
    with open(os.path.join(data_path, txt), "r") as f:
        fruits_data.append({"name":f.readline().strip(),
                            "weight":f.readline().strip(),
                            })
    
# create title of PDF
title = "Processed Updateon on" + date + "<\br>"

# create data of PDF
data = ""
for fruit in fruits_data:
    data += fruit["name"] + "<\br>" + fruit["weight"] + "<\br>"

if __name__ == "__main__":
    reports.generate_report(title, data, save_report_path)

    sender = "automation@example.com"
    replicent = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = save_report_path

    message = emails.generate_email(sender, replicent, subject, email_body, attachment_path)
    emails.send_email(message)
    

