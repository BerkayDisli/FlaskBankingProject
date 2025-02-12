# Bankin'App Web
from flask import Flask, render_template, request, session, url_for, redirect
from flask.globals import request
from functions import Bank
app = Flask(__name__)
users = {}
print(users)
app.secret_key = "scödlscojrfoıeg85"

@app.route('/')
def homepage():
    return render_template('base.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            user = Bank(session['user'])
            print(user.show_details())
            print('Login successful')
            return render_template('homepage.html')
        else:
            print('Login failed')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            print('Username already exists')
            return render_template('register.html')
        else:
            password = request.form['password']
            users[username] = password
            print("user created")
            print(users)
            return render_template('login.html')
    else:
        return render_template('register.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amount = request.form['deposit']
        user.deposit(amount)
        print(user.show_details())
        return render_template('deposit.html')

@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html')

if __name__ == '__main__':
    app.run()
