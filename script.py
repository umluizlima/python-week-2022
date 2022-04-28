from sqlmodel import select, Session

from beerlog.database import engine
from beerlog.models import Beer


with Session(engine) as session:
    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)
    session.add(brewdog)
    session.commit()
    two_chefs = Beer(name="Two Chefs", style="QPA", flavor=5, image=6, cost=6)
    session.add(two_chefs)
    session.commit()
    sql = select(Beer)
    results = session.exec(sql)
    for result in results:
        print(result)
