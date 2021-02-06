"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
wsgi_app = app.wsgi_app
app.logger.setLevel(logging.WARNING)
# streamHandler = logging.StreamHandler()
# streamHandler.setLevel(logging.WARNING)
# app.logger.addhandler(streamHandler)
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
