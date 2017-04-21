# app/__init__.py

# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


from flask_migrate import Migrate

# local imports
from config import app_config


# db initialization object used to interact with the database
db = SQLAlchemy()

# loads configuration from the config.py file
# also loads the configuration from the instance/config.py file
# imported in ~run.py
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)
    Bootstrap(app)
    from app import models


    # importing the home Blueprint
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    # importing the home Blueprint
    from .players import players as players_blueprint
    app.register_blueprint(players_blueprint)

    return app
