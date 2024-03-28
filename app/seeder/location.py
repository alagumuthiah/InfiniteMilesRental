from app.models import db, Location
from sqlalchemy import text

def seed_locations():
    locations =[
        Location(name = 'Seattle',latitude=47.6062 ,longitude= -122.3321),
        Location(name = 'San Francisco', latitude =37.7749 ,longitude=-122.4194),
        Location(name = 'New York', latitude =40.7128 ,longitude=-74.0060),
        Location(name = 'Chicago', latitude =41.8781 ,longitude=-87.6298)
    ]

    db.session.add_all(locations)
    db.session.commit()


def undo_locations():
    db.session.execute(text('TRUNCATE location RESTART IDENTITY CASCADE;'))
    db.session.commit()
