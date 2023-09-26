import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

music_catalog = Flask(__name__)
music_catalog.config.from_object(os.getenv("FLASK_ENV") or "config.settings")

db = SQLAlchemy(music_catalog)
with music_catalog.app_context():
    from .models import *
    db.create_all()

toolbar = DebugToolbarExtension(music_catalog)


from . import views
