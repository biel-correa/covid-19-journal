from flask import render_template
from app import app
from database.database import posts, states

@app.route('/', methods=['GET'])
def redirectHome():
    return home()

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', posts=posts, states=states)