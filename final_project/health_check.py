#! /usr/bin/env python3

import psutil
import emails
import socket

# set information to notify
sender = "automation@example.com"
receiver = "student@example.com"
subject_line_cpu = "Error - CPU usage is over 80%"
subject_line_disk = "Error - Available disk space is less than 20%"
subject_line_mem = "Error - Available memory is less than 100MB"
subject_line_host = "Error - localhost cannot be resolved to 127.0.0.1"
body = "Please check your system and resolve the issue as soon as possible."



# get cpu system information
cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > 80 :
    message = emails.generate_email_without_attach(sender, receiver,subject_line_cpu, body)
    emails.send_email(message)

# get disk space information
disk = psutil.disk_usage("/")
if disk.percent < 20:
    message = emails.generate_email_without_attach(sender, receiver,subject_line_disk, body)
    emails.send_email(message)

# get memory information
memory_info = psutil.virtual_memory()
availble_mem = memory_info.available
if availble_mem < 100 * 1024 * 1024: # for memory less than 100MB
    message = emails.generate_email_without_attach(sender, receiver,subject_line_mem, body)
    emails.send_email(message)

# get resolve host
host_name = socket.gethostbyname('localhost')
if host_name != '127.0.0.1': #check that can resolve to 127.0.0.1
    message = emails.generate_email_without_attach(sender, receiver,subject_line_host, body)
    emails.send_email(message)