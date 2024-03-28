from flask.cli import AppGroup

from .users import seed_users, undo_users
from .suppliers import seed_suppliers, undo_suppliers
from .category import seed_categories,undo_categories
from .location import seed_locations, undo_locations
from .pricing import seed_pricing, undo_pricing
from .cars import seed_cars,undo_cars

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed',help='to seed the database with initial data')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_suppliers()
    seed_categories()
    seed_locations()
    seed_pricing()
    seed_cars()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_suppliers()
    undo_categories()
    undo_locations()
    undo_pricing()
    undo_cars()
