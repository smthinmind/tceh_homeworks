# -*- coding: utf-8 -*-

from datetime import date
from sqlalchemy_utils import EmailType
from sqlalchemy import Table, MetaData
from slugify import slugify
from my_blog.database import db


# association table:


post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(EmailType, unique=True, nullable=False)
    user_posts = db.relationship('Post', backref=db.backref('user'))

    def __str__(self):
        return '<User %r>' % self.username


class Post(db.Model):
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

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('post', lazy="dynamic"))

    def __init__(self, user_id, title, date_created, content, is_visible, slug):
        self.user_id = user_id
        self.title = title
        self.date_created = date_created
        self.content = content
        self.is_visible = is_visible
        self.slug = slugify('-'.join([title,]))

    def __str__(self):
        return '<Post %r>' % self.title


class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    tagname = db.Column(db.String(50), unique=True, nullable=False)

    posts = db.relationship('Post', secondary=post_tags, backref=db.backref('tag', lazy="dynamic"))

    def __str__(self):
        return '<Tag %r>' % self.tagname
