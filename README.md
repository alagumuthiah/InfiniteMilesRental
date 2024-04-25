# Overview
A car rental application facilitates the convenient and efficient process of renting vehicles for short-term use. It serves as a platform connecting car owners or rental agencies with individuals seeking transportation. The application provides a user-friendly interface, streamlining the entire car rental experience from browsing available vehicles to completing the reservation.

# Steps in creating application
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
- `pipenv flask seed undo` - command to undo the seeded data in the database
