from flask import render_template
from app import app

@app.route('/post/<post_id>', methods=['GET'])
def post(post_id):
    return render_template('post.html', post_id=post_id)