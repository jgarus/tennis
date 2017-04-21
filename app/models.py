# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from app import db


class Player(db.Model):
    """
    Create a Player table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'players'

    player_name = db.Column(db.String(60), index=True, primary_key=True)
    player_yob = db.Column(db.String(60), index=True)
    grade_1 = db.Column(db.String(60), index=True, nullable=True)
    grade_a = db.Column(db.String(60), index=True, nullable=True)
    grade_2 = db.Column(db.String(60), index=True, nullable=True)
    grade_b = db.Column(db.String(60), index=True, nullable=True)
    grade_3 = db.Column(db.String(60), index=True, nullable=True)
    grade_c = db.Column(db.String(60), index=True, nullable=True)
    grade_4 = db.Column(db.String(60), index=True, nullable=True)
    grade_5 = db.Column(db.String(60), index=True, nullable=True)
    grade_6 = db.Column(db.String(50), index=True, nullable=True)


    def __repr__(self):
        return '<Player: {}>'.format(self.player_name)
