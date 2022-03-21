from flask import request, render_template
from app import app
from database.database import posts, states
from pages.posts.PostService import PostService

@app.route('/', methods=['GET'])
def redirectHome():
    return home()

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        hotPosts = PostService.getHotPosts()
        return render_template('home.html', posts=posts, states=states, hotPosts=hotPosts)
    
    if request.method == 'POST':
        data = request.form
        if data['state']:
            filteredPosts = PostService.getPostsByState(data['state'])
            hotPosts = PostService.getHotPosts(data['state'])
            return render_template('home.html', posts=filteredPosts, states=states, hotPosts=hotPosts)
        return render_template('home.html', posts=posts, states=states)