from flask import (
    abort, flash, redirect, render_template, request, session, url_for,
)

from music_catalog.controllers.utils import get_menu
from music_catalog.models import Album, Singer, Song

from ..forms.forms import LoginForm


def get_index():
    return render_template(
        "index.html",
        title="Главная страница",
        menu=get_menu(),
    )


def get_about():
    return render_template(
        "about.html",
        title="О нас",
        menu=get_menu(),
    )


def get_post_contact():
    if request.method == "POST":
        if len(request.form.get('username')) > 2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")
    return render_template(
        "contact.html",
        title="Обратная связь",
        menu=get_menu(),
    )


def get_post_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.email.data
        password = form.psw.data
        if user == "admin@mail.ru" and password == "1234":
            return redirect(url_for("profile", username="Admin"))
    flash("Некорректные авторизационные данные!", "error")
    return render_template(
        "login.html",
        tittle="Авторизация",
        menu=get_menu(),
        form=form,
    )


def get_user_profile(username):
    if "userLogged" not in session or session.get("userLogged") != username:
        abort(401)
    return render_template(
        "profile.html",
        title=f"Профиль пользователя {username}",
        menu=get_menu(),
    )


def get_user_profile_id(id):
    return render_template(
        "profile.html",
        title=f"Профиль пользователя {id}",
        menu=get_menu(),
    )


def get_singers():
    singers = Singer.query.all()
    return render_template(
        "singers.html",
        title="Исполнители",
        singers=singers,
        menu=get_menu(),
    )


def get_songs():
    songs = Song.query.all()
    return render_template(
        "songs.html",
        title="Произведения",
        songs=songs,
        menu=get_menu(),
    )


def get_albums():
    albums = Album.query.all()
    return render_template(
        "albums.html",
        title="Альбомы",
        albums=albums,
        menu=get_menu(),
    )
