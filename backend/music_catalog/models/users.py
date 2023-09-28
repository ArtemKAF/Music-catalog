from music_catalog import db
from music_catalog.models.catalogs import Base


class User(Base):
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), unique=True, nullable=False)
    is_staff = db.Column(db.Boolean(), default=False)
    db.UniqueConstraint("name", "email", )
