
from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

import locale
import os


class SignUpForm(FlaskForm):
    email = StringField(label='Set e-mail', validators=[
        validators.Email(message='Invalid e-mail')
    ])
    password = PasswordField(label='Set password', validators=[
        validators.Length(min=6, message='At least 6 characters required')
    ])
    confirm = PasswordField(label='Confirm password', validators=[
        validators.EqualTo('password', message='Passwords are not equal')
    ])


app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/')
def home():
    return 'My home page'


@app.route('/locales')
def locales():
    app_locales = dict(
        ru=locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8'),
        en=locale.setlocale(locale.LC_ALL, 'en_US.UTF-8'),
        it=locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8'),
        )
    return jsonify(app_locales)


@app.route('/sum/<int:first>/<int:second>')
def get_sum(first, second):
    return 'Your sum is {}'.format(first + second)


@app.route('/greet/<user_name>')
def greet(user_name):
    return 'Hello, {}!'.format(user_name)


@app.route('/form/user', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        print(request.form)
        form = SignUpForm(request.form)
        print(form.validate())

        if form.validate():
            message = dict(status='0 - Sucsess!')
            return jsonify(message)
        else:
            message = dict(status='1 - Error!')
            message.update(form.errors)
            return jsonify(message)

    return 'Sign Up Welcome Page'


@app.route('/serve/<path:filename>')
def read_file(filename):
    if os.path.exists('/' + filename):
        try:
            file = open('/' + filename)
            content = file.read()
            file.close()
            return content
        except:
            return 'Can\'t be read - .txt extension required'
    else:
        return '404 - File not found'


if __name__ == '__main__':
    app.run()
