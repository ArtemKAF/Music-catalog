import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

music_catalog = Flask(__name__)
music_catalog.config.from_object(os.getenv("FLASK_ENV") or "config.settings")

db = SQLAlchemy(music_catalog)
migrate = Migrate(music_catalog, db)

from . import models, views
