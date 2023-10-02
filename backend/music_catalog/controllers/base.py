from flask import (
    abort, flash, redirect, render_template, request, session, url_for,
)
from werkzeug.security import generate_password_hash

from ..forms.forms import LoginForm, RegisterForm
from ..models import Album, Singer, Song, User
from .utils import get_menu, login_required, save_in_db


@login_required
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
    if "userLogged" in session:
        return redirect(
            request.args.get("next", default=None)
            or url_for("profile", username=session.get("userLogged"))
        )
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if (
            user is not None
            or user.password_hash == generate_password_hash(form.password.data)
        ):
            session["userLogged"] = user.name
            return redirect(
                request.args.get("next", default=None)
                or url_for("profile", username=session.get("userLogged"))
            )
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
            password_hash=generate_password_hash(request.form["password"])
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


def get_logout():
    if "userLogged" in session:
        session.pop("userLogged")
    return redirect(url_for("index"))


def get_user_profile(username):
    if "userLogged" not in session or session.get("userLogged") != username:
        abort(401)
    user = User.query.filter_by(name=username).first()
    return render_template(
        "profile.html",
        title=f"Профиль пользователя {user.name}",
        user=user,
        menu=get_menu(),
    )


def get_user_profile_id(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        abort(404)
    return render_template(
        "profile.html",
        title=f"Профиль пользователя {user.name}",
        user=user,
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
