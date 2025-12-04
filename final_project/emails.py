#! /usr/bin/env python3

from email.message import EmailMessage 
import os 
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    """Create email with an attachement"""

    # set information
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # set attachment file
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1) # split only one
    
    with open(attachment_path, "rb") as file:
        message.add_attachment(
            file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=os.path.basename(attachment_path)
        )

    return message

def generate_email_without_attach(sender, recipient, subject, body):
    """Create email without an attachement"""

    # set information
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message


def send_email(message):
    """send email"""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)