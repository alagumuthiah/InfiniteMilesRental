from app.models import db, Supplier
from sqlalchemy import text

def seed_suppliers():

    suppliers =[
        Supplier(name='Hertz' , description='largest car rental companies globally, offering a wide selection of vehicles for various purposes, including leisure, business, and long-term rentals.' ),
        Supplier(name='Avis',description='provides a range of rental options, including standard cars, SUVs, trucks, and luxury vehicles'),
        Supplier(name='Budget',description=' offers affordable rental options for customers. It caters to both leisure and business travelers and provides various rental plans and discounts.'),
        Supplier(name='Alamo',description='popular choice for travelers seeking value and convenience'),
        Supplier(name='Enterprise',description='hourly car rental services in urban areas, university campuses, and corporate locations')
    ]

    db.session.add_all(suppliers)
    db.session.commit()


def undo_suppliers():
    db.session.execute(text('TRUNCATE suppliers RESTART IDENTITY CASCADE;'))
    db.session.commit()
