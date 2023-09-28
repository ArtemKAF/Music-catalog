from music_catalog import db
from music_catalog.models.catalogs import Base


class Menu(Base):
    url = db.Column(db.String(255), unique=True, nullable=False)
