from typing import List

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
