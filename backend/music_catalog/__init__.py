import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import MetaData
from flask_login import LoginManager

music_catalog = Flask(__name__)
music_catalog.config.from_object(os.getenv("FLASK_ENV") or "config.settings")

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata_obj = MetaData(naming_convention=convention)

db = SQLAlchemy(music_catalog, metadata=metadata_obj)

login_manager = LoginManager(music_catalog)
login_manager.login_view = "login"
login_manager.login_message_category = "error"

toolbar = DebugToolbarExtension(music_catalog)


from . import views
