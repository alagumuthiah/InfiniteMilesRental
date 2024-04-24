from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Car, Booking,Category,Supplier, Pricing, db
from datetime import datetime

search_routes = Blueprint('search',__name__)

@search_routes.route("/available_cars/<int:locationId>")
@login_required
def available_cars(locationId):
    search_request = request.json

    cars_in_location = Car.query.filter_by(locationId=locationId).join(Category).join(Supplier).all()

    pickup_time = datetime.strptime(search_request.get('pickupTime'), '%Y-%m-%d %H:%M:%S')
    drop_time = datetime.strptime(search_request.get('dropTime'), '%Y-%m-%d %H:%M:%S')

    bookings = Booking.query.filter(
            Booking.pickupTime <= drop_time,
            Booking.dropTime >= pickup_time
    ).all()

    booked_cars = [ #has all the cars that are booked within the given time
        booking.carId
        for booking in bookings
    ]

    car_data =[
            {
                'name':car.name,
                'category':car.category.category,
                'subcategory':car.category.subcategory,
                'supplier':car.supplier.name
            }
            for car in cars_in_location
            if car.id not in booked_cars
    ]

    return jsonify(car_data)

# Search route:

# List the available cars:
#     - LocationId - Get the cars from that locationId
#   - Bookings table - Get all the bookings with car id that overlap this time period (between the pickup time and drop time)
# Find the difference between the list of car ids (all the cars in the locatio - the booked cars during that time period)
# The difference gives the list of car details that are currently available
# overlap booking - condition - search pickup Time, drop time
# example I am searching for date 5 April to 12th April - I want to list the bookings between April 5 and April 12
