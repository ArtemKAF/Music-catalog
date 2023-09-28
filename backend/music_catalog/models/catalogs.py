from sqlalchemy.orm import declared_attr

from music_catalog import db


class Base(db.Model):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self) -> str:
        return "<{}: {}>".format(self.id, self.name)


class Singer(Base):
    albums = db.relationship(
        "Album",
        backref=db.backref("singer", lazy="joined"),
        lazy="joined",
    )


class Song(Base):
    albums = db.relationship(
        "Album",
        secondary="albums_songs",
        back_populates=("songs"),
        lazy="joined",
    )


class Album(Base):
    singer_id = db.Column(db.Integer(), db.ForeignKey("singers.id"))
    songs = db.relationship(
        "Song",
        secondary="albums_songs",
        back_populates=("albums"),
        lazy="joined",
    )


albums_songs = db.Table(
    "albums_songs",
    db.Column("album_id", db.Integer(), db.ForeignKey("albums.id")),
    db.Column("song_id", db.Integer(), db.ForeignKey("songs.id")),
    db.Column("position", db.Integer()),
)
