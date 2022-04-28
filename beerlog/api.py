from typing import List

from fastapi import FastAPI

from beerlog.core import add_beer_to_database, get_beers_from_database
from beerlog.serializers import BeerIn, BeerOut

api = FastAPI(title="Beerlog")


@api.get("/beers/", response_model=List[BeerOut])
def list_beers():
    beers = get_beers_from_database()
    return beers


@api.post("/beers/", response_model=BeerOut)
def add_beer(beer_in: BeerIn):
    return add_beer_to_database(**beer_in.dict())
