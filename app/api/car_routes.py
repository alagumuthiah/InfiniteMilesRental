from flask import Blueprint, jsonify, request
from app.models import Car, db
from flask_login import login_required
from app.decorators import is_admin
car_routes = Blueprint('cars',__name__)


@car_routes.route("/type/<string:query>/<int:id>")
def get_cars(query,id):
    if query == 'location':
        cars = Car.query.filter_by(locationId=id)

    elif query == 'category':
        cars = Car.query.filter_by(categoryId=id)

    elif query == 'supplier':
        cars = Car.query.filter_by(supplierId=id)

    else:
        return jsonify({"Error":"Query category doesn't match"})

    car_data =[
            {'id':car.id,'name':car.name}
            for car in cars
    ]

    return jsonify(car_data)


@car_routes.route("/",methods=['POST'])
@login_required
@is_admin
def add_car():
    car_info = request.json
    new_car = Car(
        name = car_info.get('name'),
        categoryId = car_info.get('categoryId'),
        supplierId = car_info.get('supplierId'),
        locationId = car_info.get('locationId'),
        gear = car_info.get('gear'),
        images = car_info.get('images',None)
    )

    db.session.add(new_car)
    db.session.commit()

    return new_car.to_dict()


@car_routes.route("/<int:car_id>",methods=['DELETE'])
@login_required
@is_admin
def delete_car(car_id):
    car_to_deleted = Car.query.get(car_id)

    if car_to_deleted:
        # Delete the record from the database session
        db.session.delete(car_to_deleted)
        db.session.commit()
        return jsonify({'message': 'Entry deleted successfully'}), 200
    else:
        return jsonify({'error': 'Entry not found'}), 404

#update the car's supplier (for instance when a car is brought by a different supplier)
@car_routes.route("/<int:car_id>/supplier",methods=["PATCH"])
def update_car_supplier(car_id):
    request_body = request.json
    car = Car.query.get(car_id)
    if car:
        car.supplierId = request_body.get('supplierId')
        db.session.commit()
        return jsonify({"message":"Car's supplier successfully updated"})
    else:
        return jsonify({'error':'No matching car id found'})

#update the car's location - when it is moved from one location to another by the supplier/ vendor
@car_routes.route("/<int:car_id>/location",methods=["PATCH"])
def update_car_location(car_id):
    request_body = request.json
    car = Car.query.get(car_id)
    if car:
        car.locationId = request_body.get('locationId')
        db.session.commit()
        return jsonify({"message":"Car's location successfully updated"})
    else:
        return jsonify({'error':'No matching car id found'})
