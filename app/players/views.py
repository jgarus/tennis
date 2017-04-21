# app/players/views.py

from flask import render_template

from . import players
from ..models import Player

@players.route('/players', defaults={'page':1})
def playerspage(page):
    players = Player.query.all()
    perpage=20
    startat=page*perpage



    return render_template('players/players.html', players=players,
                           title="Players")
