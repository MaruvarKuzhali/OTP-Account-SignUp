#This file integrates the Front end and back end working
#The flow/route of web pages are maintained here
#Flask is used and it is started, this file runs
from flask import Flask, render_template, request, flash, redirect, url_for
from csv_updates import *
from main import *
app = Flask(__name__)
app.secret_key = "abc" 
mailid = ""
forgot_pass = False

@app.route("/")
def home():
    #the start page that runs on localhost:5000. Here, it is SignUp Page
    return render_template('main.html')

@app.route("/login")
def login():
    #redirects to login page when above specified is requested from front end
    return render_template('login.html')

@app.route("/login_check", methods=['POST', 'GET'])
def login_check():
    '''
        Function Description : Works when login form gets submitted. Stores mail id for this session.
                                Check credentials and if it's correct, initiate OTP Mail. Redirect to OTP form.
                                If credentials are wrong, flash error message on the same page.

        Arguments :
            Null
        Returns :
            HTML page (if credentials correct, OTP html page. Else, flash error)
    '''
    if request.method == 'POST':
        password = request.form['psw']
        global mailid
        mailid = request.form['mailid']
        if(check_credentials(mailid, password)):
            flash("Login credentials has been verified. Please complete the OTP Verification")
            send_mail(mailid)
            return render_template('otp.html')
        else:
            flash("Invalid Username or Password")
            return render_template('login.html')

@app.route("/resend_otp", methods=['POST', 'GET'])
def resend():
    '''
        Function Description : Resends OTP to mail id if it's not NULL.
        Arguments : Null
        Returns :
            HTML Page [OTP form Page with appropriate flash message]
    '''
    if request.method == 'GET':
        if(mailid != ""):
            send_mail(mailid)
            flash('New OTP has been sent')
        else:
            flash('Email ID does not appear to be stored. Please start from initial login')
    return render_template('otp.html')

@app.route("/verify_otp", methods=['POST', 'GET'])
def verify_otp():
    '''
        Function Description : Gets user entered OTP from form. Verify the OTP. Redirects to HTML page.
        Arguments : Null                        
        Returns :
            HTML Page [If it's for forgot password, redirects to reset password page. 
                        If it's for login authentication, redirects to welcome page.]

    '''
    if request.method == 'POST':
        global forgot_pass
        otp = request.form['otp']
        if(verifyotp(otp)):
            if(forgot_pass == True):
                return render_template('reset_pass.html')
            else:
                return render_template('welcome.html')

@app.route("/reset_pass", methods=['POST', 'GET'])
def reset_pass():
    '''
        Function Description : Updates the new Password on data and flashes update message 
        Arguments : Null
        Returns :
            HTML Page [Login Page]
    '''
    if request.method == 'POST':
        password = request.form['psw']
        update_password(mailid, password)
        global forgot_pass
        forgot_pass = False
        flash("Password Changed Successful. Try logging in using new password")
    return render_template('login.html')

@app.route("/register", methods=['POST', 'GET'])
def register():
    '''
        Function Description : Gets mailid and password from new user and record it on data.
        Arguments :
            Null
        Returns :
            HTML Page (if account created successfully, shows flash message and redirects to Login Page)
    '''
    if request.method == 'POST':
        password = request.form['psw']
        mailid = request.form['mailid']
        write_csv(mailid, password)
        flash("Account creation Successful")
    return render_template('login.html')

@app.route("/forgot_pass")
def forgot_pass():
    #redirects to forgot password html page when front end requests for the above specified http path/route
    return render_template('forgot_pass.html')

@app.route("/mail_input", methods=['GET','POST'])
def mail():
    '''
        Function Description : Gets mail id from user. Check if it exists in data and sends mail. 
                                If it doesn't exist, flash error
        Arguments : Null
        Returns :
            HTML Page (OTP Form Web page) 
    '''
    global mailid, forgot_pass
    if request.method == 'POST':
        mailid = request.form['mailid']
        if(check_mailid(mailid)):
            forgot_pass = True
            send_mail(mailid)
        else:
            flash('Email ID does not exists in DataSheet. Try Signing Up!')
        return render_template('otp.html')

if __name__ == '__main__':
    app.run(debug=True)