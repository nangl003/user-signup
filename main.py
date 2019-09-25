from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def isEmpty(str):
    if len(str) == 0:
        return True
    else:
        return False

def atSignPresent(str):
    return ("@" in str)

def periodPresent(str):
    return ("." in str)

def spacePresent(str):
    return(" " in str)

@app.route('/welcome', methods=['GET','POST'])
def validate_signup():
    
    username_error = ""
    password_error = ""
    email_error = ""

    username = request.form['get-username']
    email = request.form['email']
    password = request.form['password']
    verifyPassword = request.form['verify-password']

    if isEmpty(username) or len(username) < 3 or len(username) > 20 or spacePresent(username):

        username_error = "Invalid username. Please choose a username that is between 3-20 characters long, without any spaces."     

    if not isEmpty(email) and ((len(email) < 3 or len(email) > 20) or not atSignPresent(email) or not periodPresent(email)):

        email_error = "That's not a valid email address."

    if isEmpty(password) or len(password) < 3 or len(password) > 20 or spacePresent(password):

        password_error = "Invalid password. Please choose a password that is between 3-20 characters long, without any spaces."

    elif (password != verifyPassword):

        password_error = "Your passwords do not match. Please try again."

    if not username_error and not password_error and not email_error:
        return render_template('/get-greeting.html', username = username)

    elif not username_error and not email_error and password_error:
        return render_template('/validate-signup.html', password_error=password_error, username=username, email=email)

    else:
        return render_template('/validate-signup.html', username_error=username_error, password_error=password_error, email_error=email_error)

@app.route('/')
def index():
    return render_template('/validate-signup.html')
app.run()