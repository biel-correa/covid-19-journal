from flask import request, render_template
from app import app
from pages.comments.Comment import Comment
from pages.posts.Post import Post

@app.route('/comment/<post_id>', methods=['POST'])
def commentPost(post_id):
    errors = Comment.validateData(request.form)
    data = Comment(request.form['name'], request.form['email'], request.form['content'])
    if len(errors) == 0:
        Post.commentPost(post_id, data)
    return render_template('post.html', post=Post.getPostById(post_id), errors=errors)