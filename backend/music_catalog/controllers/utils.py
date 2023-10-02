from typing import Callable, List

from flask import redirect, request, session, url_for

from music_catalog import db
from music_catalog.models import Menu


def get_menu() -> List[Menu]:
    return Menu.query.all()


def save_in_db(obj) -> None:
    try:
        db.session.add(obj)
        db.session.flush()
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        raise Exception("Ошибка сохранения в БД!", error)


def login_required(func: Callable):
    def wrapper(*args, **kwargs):
        if "userLogged" in session:
            return func(*args, **kwargs)
        return redirect(url_for("login", next=request.url))
    return wrapper
