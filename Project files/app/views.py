import logging
from flask import render_template
from app import app, db, models

@app.route ('/', methods = ['GET'])
def index ():
    return render_template('index.html')

@app.route ('/getstarted', methods = ['GET','POST'])
def gettingstarted ():
    return render_template('form.html')

@app.route ('/dashboard', methods = ['GET','POST'])
def dashboard ():
    return render_template('dashboard.html')
