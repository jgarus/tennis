# app/home/vies.py

from flask import render_template

from . import home

@home.route('/')
def homepage():
    # render home template

    return render_template('home/index.html', title="Tennis")
