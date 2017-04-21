# app/players/views.py
from flask_paginate import Pagination
from flask import render_template

from . import players
from ..models import Player


@players.route('/players', defaults={'page':1}, methods=["GET"])
@players.route('/players/<int:page>', methods=["GET"])
def playerspage(page):
    per_page=20

    # paginated = Player.query.paginate(page,per_page, False)
    players = Player.query.paginate(page, per_page, False)

    return render_template('players/players.html', players=players,
                           title="Players")
