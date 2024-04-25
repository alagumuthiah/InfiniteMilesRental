## Overview

A car rental application facilitates the convenient and efficient process of renting vehicles for short-term use. It serves as a platform connecting car owners or rental agencies with individuals seeking transportation. The application provides a user-friendly interface, streamlining the entire car rental experience from browsing available vehicles to completing the reservation.

## Project setup

To run the application locally:
1. Git clone the repo `https://github.com/alagumuthiah/InfiniteMilesRental.git`
2. Use pipenv install Flask to install flask
3. Create a directory named app and __init__.py
4. Initialize the app using __name__
5. `pipenv install python-dotenv`
6. Create .env file and .flaskenv file
7. Create a config file to load the environment variables
8. use command `pipenv run flask run --port 8000`
9. Create the database and store the database url in the .env file
10. Initialize Alembic environment using `pipenv run flask db init`
11. Run the command `pipenv run flask db migrate -m "create <table_name> table"` to create migration file
12. `pipenv run flask db upgrade` command to run the migration
13. `pipenv flask seed all` - command to seed the database with initial data
14. `pipenv flask seed undo` - command to undo the seeded data in the database


## Technologies USed

**FrontEnd**
- React
- Redux
- HTML
- Tailwind CSS
- Javascript

**Backend**
- Flask
- Python
- SQLAlchemy
- PostgreSQL

**API**
- Payment Gateway - TBD

## Features of the App

* User can signUp/ Login
* Users can check the availability of the cars for the specific date and time.
* Users can apply various filters like category, supplier to find car based on their needs.
* Users can pay online via payment gateway in advance for their booking.
* Admin User can update the car's status(Active when picked up and Completed when dropped off)

## Link to Wiki docs

[Link to Wiki Docs] [https://github.com/alagumuthiah/InfiniteMilesRental/wiki]

<!-- # Steps in creating application
- Run npx create-react-app to scaffold the React application
- Use pipenv install Flask to install flask
- Create a directory named app and __init__.py
- Initialize the app using __name__
- `pipenv install python-dotenv`
- create .env file and .flaskenv file
- Create a config file to load the environment variables
- create a basic route.
- use command `pipenv run flask run --port 8000`
- Create the database and store the database url in the .env file
- Use alembic to create tables in database
- To use alembic - first create a model file that have a class representing a model
- Initialize Alembic environment using `pipenv run flask db init`
- Run the command `pipenv run flask db migrate -m "create <table_name> table"` to create migration file
- `pipenv run flask db upgrade` command to run the migration
- `pipenv flask seed all` - command to seed the database with initial data
- `pipenv flask seed undo` - command to undo the seeded data in the database -->
