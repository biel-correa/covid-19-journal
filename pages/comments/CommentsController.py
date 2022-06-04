from xml.etree.ElementTree import Comment
from flask import request, redirect, url_for
from app import app
from pages.posts.Post import Post

@app.route('/comment/<post_id>', methods=['POST'])
def commentPost(post_id):
    data = Comment(request.form['name'], request.form['email'], request.form['content'])
    result = Post.commentPost(post_id, data)
    if type(result) == Post:
        return redirect(url_for('post', post_id=post_id))
    return redirect(url_for('home'))