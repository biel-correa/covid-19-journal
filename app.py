from flask import Flask

app = Flask(__name__)

from pages.home import HomeController

if __name__ == '__main__':
    app.run(debug=True)