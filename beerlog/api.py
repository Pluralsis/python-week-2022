from typing import List  # [missing-module-docstring]

from fastapi import FastAPI  # Protocol ASGI

from beerlog.core import get_beers_from_database
from beerlog.database import get_session
from beerlog.models import Beer
from beerlog.serializers import BeerIn, BeerOut

api = FastAPI(title='Beerlog')


@api.get('/beers', response_model=List[BeerOut])
async def list_beers():  # [missing-module-docstring]
    beers = get_beers_from_database()
    return beers


@api.post('/beers', response_model=BeerOut)
async def add_beer(beer_in: BeerIn):  # [missing-module-docstring]
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)
    return beer
