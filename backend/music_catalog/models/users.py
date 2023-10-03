from flask_login import AnonymousUserMixin, UserMixin

from music_catalog import db, login_manager
from music_catalog.models.catalogs import Base


class User(UserMixin, Base):
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), unique=True, nullable=False)
    is_staff = db.Column(db.Boolean(), default=False)
    db.UniqueConstraint("name", "email", )


class AnonymousUser(AnonymousUserMixin):
    pass


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
