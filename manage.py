# run.py

import os

from app import create_app

# the configuration name we are passing to the create_app function
config_name = os.getenv('FLASK_CONFIG')

# assigning it to variable app
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
