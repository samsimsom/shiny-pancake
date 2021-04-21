

from flask import render_template, redirect, url_for, session
from app.main import main


@main.route('/')
def index():
    session['user'] = 'samsimsom'
    return 'Hello World!'


@main.route('/get')
def get_session():
    return session['user']
