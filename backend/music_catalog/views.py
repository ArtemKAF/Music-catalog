from music_catalog import music_catalog
from music_catalog.controllers.base import (
    get_about, get_albums, get_index, get_post_contact, get_post_login,
    get_singers, get_songs, get_user_profile, get_user_profile_id,
)


@music_catalog.route("/")
def index():
    return get_index()


@music_catalog.route("/about")
def about():
    return get_about()


@music_catalog.route("/contact", methods=["GET", "POST", ])
def contact():
    return get_post_contact()


@music_catalog.route("/login", methods=["GET", "POST", ])
def login():
    return get_post_login()


@music_catalog.route("/profile/<username>")
def profile(username):
    return get_user_profile(username)


@music_catalog.route("/profile/<int:id>")
def prof(id):
    return get_user_profile_id(id)


@music_catalog.route("/singers", methods=["GET", "POST", ])
def singers():
    return get_singers()


@music_catalog.route("/songs", methods=["GET", "POST", ])
def songs():
    return get_songs()


@music_catalog.route("/albums", methods=["GET", "POST", ])
def albums():
    return get_albums()
