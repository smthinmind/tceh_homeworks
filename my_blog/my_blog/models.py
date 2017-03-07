# -*- coding: utf-8 -*-

from datetime import date

from sqlalchemy_utils import EmailType

from sqlalchemy import Table, MetaData

from slugify import slugify

from my_blog.app import db


# association table:

metadata = MetaData()

posts_tags = Table('posts_tags', db.Model.metadata,
    db.Column('post_id', db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.ForeignKey('tag.id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(EmailType, unique=True, nullable=False)
    posts = db.relationship('Post', back_populates='user')

    def __str__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
        index=True
    )

    title = db.Column(db.String(140), unique=True, nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    slug = db.Column(db.String(200))
    content = db.Column(db.String(10000), nullable=False)
    is_visible = db.Column(db.Boolean, default=True)

    user = db.relationship('User', back_populates='posts')
    tags = db.relationship('Tag', secondary=posts_tags, back_populates='posts')

    def __str__(self):
        return '<Post %r>' % self.title

    def __init__(self, user_id, title, date_created, content, is_visible, slug):
        self.user_id = user_id
        self.title = title
        self.date_created = date_created
        self.content = content
        self.is_visible = is_visible
        self.slug = slugify('-'.join([title, ]))



class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    tagname = db.Column(db.String(50), unique=True, nullable=False)

    posts = db.relationship('Post', secondary=posts_tags, back_populates='tags')

    def __str__(self):
        return '<Tag %r>' % self.tagname
