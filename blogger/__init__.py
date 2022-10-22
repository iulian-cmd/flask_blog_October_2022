from flask import Flask  # Import Flask to allow us to create our app
from flask.ext.sqlalchemy import SQLAlchemy  # Import SQLAlchemy
from flask.ext.login import LoginManager    # Import LoginManager
from os import path                    # Import path to help us with our file paths


def create_app():
    # Create a new instance of the Flask class called "app"
    app = Flask(__name__)

    return app
