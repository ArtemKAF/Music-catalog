from flask import (abort, flash, redirect, render_template, request, session,
                   url_for)


def get_index():
    return render_template(
        "index.html",
        title="Главная страница",
    )


def get_about():
    return render_template(
        "about.html",
        title="О нас",
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
    )


def get_post_login():
    if "userLogged" in session:
        return redirect(url_for("profile", username=session.get("userLogged")))
    elif (
        request.method == "POST"
        and request.form.get("username") == "admin"
        and request.form.get("psw") == "admin"
    ):
        session["userLogged"] = request.form.get("username")
        return redirect(url_for("profile", username=session.get("userLogged")))
    return render_template(
        "login.html",
        tittle="Авторизация",
    )


def get_user_profile(username):
    if "userLogged" not in session or session.get("userLogged") != username:
        abort(401)
    return render_template(
        "profile.html",
        title=f"Профиль пользователя {username}",
    )


def get_user_profile_id(id):
    return render_template(
        "profile.html",
        title=f"Профиль пользователя {id}",
    )


def get_singers():
    return render_template(
        "singers.html",
        title="Исполнители",
    )
