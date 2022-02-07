from flask import render_template
from app import app

@app.route('/', methods=['GET'])
def redirectHome():
    return None

@app.route('/home', methods=['GET'])
def home():
    return None