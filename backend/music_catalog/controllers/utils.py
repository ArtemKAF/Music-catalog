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
        details = details_db_error(repr(error))
        raise Exception("Ошибка сохранения в БД!", details)


def details_db_error(error: str) -> str:
    details = error.split("DETAIL:  ")[-1].split("\\n")[0]
    return details
