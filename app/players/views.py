# app/players/views.py

from flask import render_template

from . import players

@players.route('/players')
def playerspage():
    from app import models
    # render home template

   #con = sql.connect("database.db")
   # con.row_factory = sql.Row
   #
   # cur = con.cursor()
   # cur.execute("select * from players")
   #
  # rows = cur.fetchall();
  # return render_template("list.html",rows = rows)
    return render_template('players/players.html', players = players.query.all())

    #return render_template('players/players.html', title="Players")
