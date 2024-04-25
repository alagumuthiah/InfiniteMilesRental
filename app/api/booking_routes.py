from flask import Blueprint, jsonify, request
from app.models import Booking, db
from flask_login import login_required, current_user
from app.decorators import is_admin

booking_routes =Blueprint('bookings',__name__)


@booking_routes.route("/user/<int:user_id>")
@login_required
def get_bookings_by_user_id(user_id):
    if current_user.id == user_id:
        bookings = Booking.query.filter_by(userId=user_id).all()

        # Convert the SQLAlchemy objects to a dictionary for JSON serialization
        bookings_data = [
            booking.to_dict()
            for booking in bookings
        ]
        return jsonify(bookings_data)
    else:
        return jsonify({"error":"You can view only your bookings, Bad Request"}), 400


# {
#     "email":"john.doe@gmail.com",
#     "userId":"1",
#     "pickupLocation":"Seattle",
#     "pickupTime":"2024-04-03 12:00:00",
#     "dropLocation":"Seattle",
#     "dropTime":"2024-04-10 12:00:00",
#     "carId":1,
#     "categoryId":1,
#     "status":"Inactive",
#     "protected":true,
#     "cost":150,
#     "paymentMethod":"Paypal"

# }

@booking_routes.route("/",methods=["POST"])
@login_required
def create_booking():
    booking_info = request.json #required data for creating a booking is passed as JSON in request body
    new_booking = Booking(
        email = booking_info.get('email'),
        userId = booking_info.get('userId'),
        pickupLocation = booking_info.get('pickupLocation'),
        pickupTime = booking_info.get('pickupTime'),
        dropLocation = booking_info.get('dropLocation'),
        dropTime = booking_info.get('dropTime'),
        carId = booking_info.get('carId'),
        categoryId = booking_info.get('categoryId'),
        status = 'Inactive',
        protected = booking_info.get('protected'),
        cost = booking_info.get('cost'),
        paymentMethod = booking_info.get('paymentMethod')
    )

    db.session.add(new_booking)
    db.session.commit()

    return new_booking.to_dict()


@booking_routes.route("/<int:booking_id>")
def get_bookings_by_booking_id(booking_id):
    bookings = Booking.query.filter_by(id=booking_id).all()
    if bookings:
        if bookings.userId == current_user.id:
        # Convert the SQLAlchemy objects to a dictionary for JSON serialization
            bookings_data = [
                booking.to_dict()
                for booking in bookings
                ]
            return jsonify(bookings_data)
        else:
            return jsonify({"error":"You can view only your bookings, Bad Request"}), 400
    else:
            return jsonify({"error":"No Bookings yet"}), 400


@booking_routes.route("/<int:booking_id>",methods=["PUT"])
@login_required
def update_booking(booking_id):
    bookings = Booking.query.get(booking_id)
    if bookings and bookings.userId==current_user.id:
        update_request = request.json #the entire record info that needs to be updated is passed
        updated_booking = bookings.update(update_request)
        db.session.commit()
        return jsonify({'message':'record successfully updated'})
    else:
        return jsonify({'error':'No matching booking found'})


#update the booking status to active/ cancelled, etc
@booking_routes.route("/<int:booking_id>",methods=["PATCH"])
@login_required
@is_admin
def update_booking_status(booking_id):
    booking_status = request.json
    # print(booking_status.status)
    bookings = Booking.query.get(booking_id)
    print(bookings.to_dict())
    if bookings:
        bookings.status = booking_status.get('status')#fetching status from request body
        db.session.commit()
        return jsonify({'message':'Booking status successfully updated'})
    else:
        return jsonify({'error':'No matching booking id found'})
