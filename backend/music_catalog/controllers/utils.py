from typing import List

from music_catalog.models import Menu


def get_menu() -> List[Menu]:
    return Menu.query.all()
