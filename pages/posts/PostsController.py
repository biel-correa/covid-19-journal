from flask import render_template
from app import app
from pages.posts.Post import Post

@app.route('/post/<post_id>', methods=['GET'])
def post(post_id):
    return render_template('post.html', post=Post.getPostById(post_id))