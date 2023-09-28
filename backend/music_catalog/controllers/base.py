from flask import (
    abort, flash, redirect, render_template, request, session, url_for,
)

from music_catalog.controllers.utils import get_menu, save_in_db
from music_catalog.forms.forms import LoginForm, RegisterForm
from music_catalog.models import Album, Singer, Song, User


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
    form = LoginForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == "admin@mail.ru" and password == "1234":
            return redirect(url_for("profile", username="Admin"))
        else:
            flash("Некорректные авторизационные данные!", "error")
    return render_template(
        "login.html",
        tittle="Авторизация",
        menu=get_menu(),
        form=form,
    )


def get_post_register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User(
            name=request.form["name"],
            email=request.form["email"],
            password_hash=request.form["password"]
            )
        try:
            save_in_db(user)
        except Exception as error:
            flash(
                f"{error.args[0]} - {error.args[1]}",
                category="error"
            )
        return redirect(url_for("login"))
    else:
        flash("Некорректные регистрационные данные!", "error")
    return render_template(
        "register.html",
        tittle="Регистрация",
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
