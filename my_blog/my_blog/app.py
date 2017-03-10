
from flask import Flask
from my_blog.views import views, admin
from my_blog.database import db

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.update({
        'DEBUG': True,
        'SECRET_KEY': 'My secret key',
        'WTF_CSRF_ENABLED': False,
        # Database settings:
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///blog.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    })

    app.register_blueprint(views)
    app.register_blueprint(admin)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()