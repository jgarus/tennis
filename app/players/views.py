# app/players/views.py

from flask import render_template

from . import players

@players.route('/players')
def playerspage():
    # render home template

    return render_template('players/players.html', title="Players")
