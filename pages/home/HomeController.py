from flask import render_template
from app import app

@app.route('/', methods=['GET'])
def redirectHome():
    return home()

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')