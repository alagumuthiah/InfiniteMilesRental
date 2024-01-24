This is the planning phase for the application.

# Overview

InfiniteMilesRental - a car rental application that lists different car rentals in one place

# Style
- Color Palette - #355070, #6D597A, #B56576, #E56B6F, #EAAC8B
- Color Palette - #8ECAE6, #219EBC, #023047, #FFB703, #FB8500
- Font - TBD

# User types:
* User types:
    - Normal User
    - Admin User

# Features of the APP
* User can signUp/ Login
* Use OAuth for Authentication and JSON web tokens
* Display the available cars based on the Pickup location, pickup time, drop location and drop time
* Apply various filters like Location, cost per day, free cancellation, etc
* Filters based on the car Size, sort by options
* Selecting a car, displays detailed information about the selected car
* Provide details like driver's details, billing address, payment mode

# UI Pages for the App

* Home page
    - displays the option to select pickup and drop locations
    - displays the brands for rental cars supported by this site
    - Highlights the features for renting a car like Flexible rentals, No hidden fees, etc

* Header:
    - Logo
    - Manage Booking - given the email and booking id- displays the details of the booking
    - Log In

* Footer
    - Navigation to other pages in the App
    - Connect us with (Social Media Links)
    - Copyrights
    - Change Language Feature (Optional feature)

* Sign Up
    - Card that displays signup options
    - Supports OAuth - Google, github or Create a new Account
* Login
    - Card that displays Login form - Requesting username and Password

* Display all cars
    - Display the list of cars along with various filters on the left side bar and top

* Car detail Page
    - Displays the car details when selected
    - Cost involved- what are the features avilable for the selected car

* Protected option
    - Displays the list of options available for protection to the car
    - Select / deselect the different options and continue to book

* Payment page
    - This shows the details of the booking and the payment option
    - Fill in the driver's details, billing address and payment details


# DB Schema

- User
    * id
    * firstname
    * lastname
    * email
    * hashedPassword
    * loginMethod - traditional, google, github, facebook

- Booking
    * bookingId
    * email
    * userId (foreign key from User table)
    * pickup location
    * pickup time
    * drop location
    * drop time
    * carId - foreign key from car table
    * protected - boolean
    * cost (cost of the booking)

- Cars
    * Id
    * Name
    * SupplierId (Foreign Key)
    * Category (ENUM)
    * Gear (Automatic/Manual)
    * Seats
    * Bags
    * Price (for a Day)
    * Images
    * Booked - boolean
    * locationId (Foreign Key)

Check on how to account for cars which will be dropped at a location in the future date

- Supplier
    * id
    * name
    * description

- Location
    * Id
    * Name
    * Map coordinates

- Reviews
    * ReviewId
    * UserID (Foreign Key)
    * CarId (Foreign Key)
    * Star Review (out of 10)
    * Value for Money (out of 10)
    * Car cleanliness (out of 10)
    * Car condition (out of 10)
    * Pick up speed (out of 10)

- Transaction
    * id
    * bookingId
    * payment method

Associations:
 - A User can make many bookings
 - Booking belongs to a Car and a User
 - A supplier can hav emany cars
 - Car belongs to a Supplier
 - Car belongs to a Location
 - Location can have many cars
 - Car can have many reviews
 - User can write many reviews
 - A Review belongs to a user and a car.
 - One to one relationship between transaction and booking

# Backend Routes:

`Users`

* POST /users/login
* POST /users/signup
* DELETE /users/logout

`Bookings`

* GET /bookings
* POST /bookings - create an entry in the booking table when a user books a vehicle for rent
* GET /bookings/:bookingId
* GET /bookings/user/:userId (Booking history of the user)
* PUT /bookings/:bookingId- update a booking (like including a protected plan/ removing)
* DELETE /bookings/:bookingId- - cancel a booking

`Cars`

* GET /cars/suppliers/:supplierId (not booked)
* GET /cars/category/&searchparams (not booked)
* GET /cars/location/:locationId (not booked)
* POST /cars - when a new car is included as part of the rental
* PUT /cars/:carId - update when a car is booked
* PUT /cars/location/:locationId - update locationID and booked to false when a car is dropped off at a location
* DELETE /cars/:cardId - remove car from the rental list
