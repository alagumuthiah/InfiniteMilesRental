from flask import Blueprint, jsonify, request
from app.models import Booking, db

booking_routes =Blueprint('bookings',__name__)


@booking_routes.route("/user/<int:user_id>")
def get_bookings_by_user_id(user_id):
    bookings = Booking.query.filter_by(userId=user_id).all()
    # Convert the SQLAlchemy objects to a dictionary for JSON serialization
    bookings_data = [
        {'id': booking.id, 'user_id': booking.userId, 'category':booking.categoryId}
        for booking in bookings
        ]
    return jsonify(bookings_data)


@booking_routes.route("/",methods=["POST"])
def create_booking():
    booking_info = request.json #required data for creating a booking is passed as JSON in request body

    new_booking = Booking(
        email = booking_info['email'],
        userId = booking_info['userId'],
        pickupLocation = booking_info['pickupLocation'],
        pickupTime = booking_info['pickupTime'],
        dropLocation = booking_info['dropLocation'],
        dropTime = booking_info['dropTime'],
        carId = booking_info['carId'],
        categoryId = booking_info['categoryId'],
        status = 'Inactive',
        protected = booking_info['protected'],
        cost = booking_info['cost'],
        paymentMethod = booking_info['paymentMethod']
    )

    db.session.add(new_booking)
    db.session.commit()

    return new_booking.to_dict()


@booking_routes.route("/<int:booking_id>")
def get_bookings_by_booking_id(booking_id):
    bookings = Booking.query.filter_by(id=booking_id).all()
    # Convert the SQLAlchemy objects to a dictionary for JSON serialization
    bookings_data = [
        {'id': booking.id, 'user_id': booking.userId, 'category':booking.categoryId}
        for booking in bookings
        ]
    return jsonify(bookings_data)


@booking_routes.route("/<int:booking_id>",methods=["PUT"])
def update_booking(booking_id):
    bookings = Booking.query.get(booking_id)
    if bookings:
        update_request = request.json #the entire record info that needs to be updated is passed
        updated_booking = bookings.update(update_request)
        db.session.commit()
        return jsonify({'message':'record successfully updated'})
    else:
        return jsonify({'error':'No matching booking id found'})


#update the booking status to active/ cancelled, etc
@booking_routes.route("/<int:booking_id>",methods=["PATCH"])
def update_booking_status(booking_id):
    booking_status = request.json
    bookings = Booking.query.get(booking_id)
    if bookings:
        bookings.status = booking_status.status #fetching status from request body
        db.session.commit()
        return jsonify({'message':'Booking status successfully updated'})
    else:
        return jsonify({'error':'No matching booking id found'})
