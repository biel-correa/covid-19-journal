from flask import render_template, redirect, url_for
from app import app
from pages.posts.Post import Post

@app.route('/post/<post_id>', methods=['GET'])
def post(post_id):
    return render_template('post.html', post=Post.getPostById(post_id))

@app.route('/posts/like/<post_id>', methods=['GET'])
def likePost(post_id):
    result = Post.likePost(post_id)
    if type(result) == Post:
        return redirect(url_for('post', post_id=post_id))
    return redirect(url_for('home'))

@app.route('/posts/dislike/<post_id>', methods=['GET'])
def dislikePost(post_id):
    result = Post.dislikePost(post_id)
    if type(result) == Post:
        return redirect(url_for('post', post_id=post_id))
    return redirect(url_for('home'))
