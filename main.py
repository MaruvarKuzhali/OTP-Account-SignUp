#This python file deals with OTP Generation and sending Email
import config #mail id and App Password are stored in config file
import os
import math
import random
import smtplib
import ssl
import csv
from email.mime.text import MIMEText

OTP = ""
def generate_otp():
    '''
        Function Description : This function generates OTP, defines the message to be sent in mail.
        Arguments :
            Null
        Returns :
            otp_msg = string (mail body along with OTP)
    '''
    digits="0123456789"
    global OTP
    OTP = ""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp_msg = OTP + " is your OTP for Authentication. OTP will expire in 5 minutes."
    return otp_msg

#s = smtplib.SMTP('smtp.gmail.com', 587)
#s.starttls()
def send_mail(emailid):
    '''
        Function Description : This function opens SMPT SSL connection using email id ('FROM' email id) and
        it's app password. And also sends the OTP generated to the user entered email id
        Arguments :
            emailid = string ("To" email id)
        Returns :
            Null
    '''
    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL('smtp.gmail.com', port=0, context=context)
    s.login(config.email_id, config.App_secret_key)
    msg = MIMEText(generate_otp())
    msg['Subject'] = "OTP VERIFICATION MAIL"
    msg['From'] = config.email_id
    msg['To'] = emailid
    s.sendmail(config.App_secret_key,emailid,msg.as_string())
    return

def verifyotp(a):
    '''
        Function Description : Checks the correctness of user entered OTP
        Arguments :
            a = string (User entered OTP)
        Returns :
            Integer (1 if it matches, 0 if the OTPs don't match)
    '''
    if a == OTP:
        return 1
    else:
        return 0


    
