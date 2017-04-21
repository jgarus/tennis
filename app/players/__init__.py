# app/home/__init__.py
from flask import Blueprint

# iniializing Blueprint object
players = Blueprint('players', __name__)

# importing views from ../views.py
from . import views
