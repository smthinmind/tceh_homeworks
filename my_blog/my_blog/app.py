
from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import my_blog.config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from my_blog.models import Post
    from my_blog.forms import PostForm

    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()
            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template('home.txt', posts=posts)


@app.route('/<string:post_slug>/', methods=['GET', ])
def post(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    return render_template('post.txt', post=post)

if __name__ == '__main__':
    from my_blog.models import *
    db.create_all()

    app.run()
