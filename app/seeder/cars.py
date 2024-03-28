from app.models import db, Car
from sqlalchemy import text

def seed_cars():
    cars = [
        Car(name= 'Toyota Camry',
            categoryId= 1,
             supplierId= 2,
             gear= 'Automatic',
             locationId = 1),
        Car(name= 'BMW 3 Series',
            categoryId= 1,
             supplierId= 3,
             gear= 'Automatic',
             locationId = 1),
        Car(name= 'Honda Civic',
            categoryId= 2,
             supplierId= 4,
             gear= 'Manual',
             locationId = 1),
        Car(name= 'Audi',
            categoryId= 2,
             supplierId= 1,
             gear= 'Automatic',
             locationId = 2),
        Car(name= 'Mercedes-Benz C-Class',
            categoryId= 3,
             supplierId= 2,
             gear= 'Manual',
             locationId = 3),
        Car(name= 'Ford Mustang',
            categoryId= 4,
             supplierId= 4,
             gear= 'Automatic',
             locationId =2),
        Car(name= 'Nissan Altima',
            categoryId= 6,
             supplierId= 3,
             gear= 'Manual',
             locationId = 3),
        Car(name= 'Subaru Outback',
            categoryId= 6,
             supplierId= 2,
             gear= 'Automatic',
             locationId = 4),
        Car(name= 'Dodge Charger',
            categoryId= 3,
             supplierId= 2,
             gear= 'Automatic',
             locationId =3),
        Car(name= 'Kia Soul',
            categoryId= 1,
             supplierId= 2,
             gear= 'Manual',
             locationId = 1),
    ]

    db.session.add_all(cars)
    db.session.commit()

def undo_cars():
    db.session.execute(text('TRUNCATE cars RESTART IDENTITY CASCADE;'))
    db.session.commit()
