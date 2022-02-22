from flask import Flask

app = Flask(__name__)

from pages.home import HomeController
from pages.posts import PostsController

if __name__ == '__main__':
    app.run(debug=True)