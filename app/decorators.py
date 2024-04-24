from functools import wraps
from flask import abort
from flask_login import current_user

# def is_owner(func):
#     @wraps(func)
#     def decorated_function(*args, **kwargs):
#         # Assuming the record ID is passed as a URL parameter
#         record_id = kwargs.get('')

#         # Check if the logged-in user is the owner of the record
#         if current_user.is_authenticated and current_user.id == record_owner_id:
#             return func(*args, **kwargs)
#         else:
#             # If the user is not the owner, return a 403 Forbidden error
#             abort(403)

#     return decorated_function

def is_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.isAdmin==True:
            return func(*args,**kwargs)
        else:
            #the logged in user is not an admin so prohibited form accessing the route
            abort(403)

    return decorated_function

# - I need to create a column isAdmin(boolean) in users table
# - Modify the User models file by updating the column, now run the db migrate command
# - this creates a revision file. Now update the generated upgrade and downgrade functions in the revision
# - Then run db upgrade - this updates the table with the column specified
