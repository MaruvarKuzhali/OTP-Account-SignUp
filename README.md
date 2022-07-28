# OTP Verfication Application
***
This project implements a simple OTP Verification via email messages. A new user can start with creating an account. Whenever user tries to login, OTP verification is done as a second factor authentication. The OTP is sent via mail to the user registered email id using python smtplib library. OTP will be expired in 5 minutes. Javascript is used to disable the form submission after 5 minutes. If user forgets password, forgot password option can be used to reset password. OTP verification is done before resetting the password.
## Flow Diagram
The following diagram briefly shows the flow of the system
![alt text](./templates/flow.png)
## How to Use
* First install the required libraries mentioned in requirements.txt
```bash
pip install requirements.txt
```
* Create config.py file and add the email id, mail's app password and passlib context which is used for hasing password
* Create Datasheet.csv file with fields Email_id and Password
* Start running the flask server
```bash
python -m flask run
```
By default, web application will be deployed using port 5000. So, the home page will be displayed on "http://localhost.com:5000"