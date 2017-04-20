# app/home/__init__.py

from flask import Blueprint

# initializing Blueprint object
home = Blueprint('home', __name__)

# importing views from ../views.py
from . import views
