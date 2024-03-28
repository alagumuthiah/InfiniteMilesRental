from app.models import db, Pricing
from sqlalchemy import text

def seed_pricing():
    pricings = [
        Pricing(categoryId= 1,
                supplierId= 2,
                locationId= 1,
                price= 40,
                protectionCost=15),
        Pricing(categoryId= 1,
                supplierId= 3,
                locationId= 1,
                price= 70,
                protectionCost=20),
        Pricing(categoryId= 2,
                supplierId= 4,
                locationId= 1,
                price= 60,
                protectionCost=18),
        Pricing(categoryId= 2,
                supplierId= 1,
                locationId= 2,
                price= 100,
                protectionCost=30),
        Pricing(categoryId= 3,
                supplierId= 2,
                locationId= 3,
                price= 80,
                protectionCost=12),
        Pricing(categoryId= 4,
                supplierId= 4,
                locationId= 2,
                price= 60,
                protectionCost=15),
        Pricing(categoryId= 6,
                supplierId= 3,
                locationId= 3,
                price= 70,
                protectionCost=10),
        Pricing(categoryId= 6,
                supplierId= 2,
                locationId= 4,
                price= 55,
                protectionCost=10),
    ]

    db.session.add_all(pricings)
    db.session.commit()

def undo_pricing():
    db.session.execute(text('TRUNCATE pricing RESTART IDENTITY CASCADE;'))
    db.session.commit()
