from flask import request, render_template
from app import app
from pages.posts.Post import Post

@app.route('/', methods=['GET'])
def redirectHome():
    return home()

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        hotPosts = Post.getHotPosts()
        posts = Post.getAllPosts()
        states = Post.getAllStates()
        return render_template('home.html', posts=posts, states=states, hotPosts=hotPosts)
    
    if request.method == 'POST':
        data = request.form
        if data['state']:
            filteredPosts = Post.getPostsByState(data['state'])
            hotPosts = Post.getHotPosts(data['state'])
            states = Post.getAllStates()
            return render_template('home.html', posts=filteredPosts, states=states, hotPosts=hotPosts)
        return render_template('home.html', posts=posts, states=states)