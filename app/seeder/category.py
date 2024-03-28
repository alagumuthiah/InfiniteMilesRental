from app.models import db, Category
from sqlalchemy import text

def seed_categories():

    categories =[
        Category(category= 'Car',
                 subcategory = 'Economy',
                 seats =5),
        Category(category= 'Car' ,
                 subcategory = 'Compact',
                 seats = 5),
        Category(category= 'Car',
                 subcategory = 'Standard',
                 seats =5),
        Category(category= 'Car',
                 subcategory = 'Premium',
                 seats =5),
        Category(category= 'Car',
                 subcategory = 'Luxury',
                 seats =5),
        Category(category= 'SUV',
                 subcategory = 'Compact',
                 seats =5),
        Category(category= 'SUV',
                 subcategory = 'Standard',
                 seats = 7),
        Category(category= 'SUV',
                 subcategory = 'Premium',
                 seats =8),
        Category(category= 'SUV',
                 subcategory = 'Luxury',
                 seats = 5),
        Category(category= 'Van',
                 subcategory = 'Mini Van',
                 seats = 7),
        Category(category= 'Van',
                 subcategory = 'Van',
                 seats = 15),
    ]

    db.session.add_all(categories)
    db.session.commit()

def undo_categories():
    db.session.execute(text('TRUNCATE categories RESTART IDENTITY CASCADE;'))
    db.session.commit()
