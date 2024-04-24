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
        if current_user.is_authenticated and current_user.email=='admin@gmail.com':
            return func(*args,**kwargs)
        else:
            #the logged in user is not an admin so prohibited form accessing the route
            abort(403)

    return decorated_function
