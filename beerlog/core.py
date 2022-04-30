from typing import List
from sqlmodel import select

from beerlog.database import get_session
from beerlog.models import Beer


def add_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int,
) -> bool:
    beer = Beer(
        name=name,
        style=style,
        flavor=flavor,
        image=image,
        cost=cost,
    )
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    return beer


def get_beers_from_database() -> List[Beer]:
    with get_session() as session:
        sql = select(Beer)
        return list(session.exec(sql))
