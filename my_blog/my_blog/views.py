
from flask import Blueprint, request, render_template, flash
from my_blog.models import Post
from my_blog.forms import PostForm
from my_blog.database import db

views = Blueprint('views', __name__)
admin = Blueprint('admin', __name__, url_prefix='/admin')

# Views


@views.route('/', methods=['GET', 'POST'])
def index():
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
    print(posts)
    return render_template('home.txt', posts=posts)


@views.route('/<string:post_slug>/', methods=['GET', ])
def post(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    print(post, post_slug)
    return render_template('post.txt', post=post)


# Admin pages
