# # Function to hash a password
# def hash_password(password):
#     # Generate a salt and hash the password with bcrypt
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#     return hashed_password

# # Function to verify a password against a hashed password
# def verify_password(password, hashed_password):
#     # Check if the password matches the hashed password using bcrypt
#     return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# # Example usage
# password = "secret_password"
# hashed_password = hash_password(password)
# print("Hashed password:", hashed_password)

# # Verify the password
# is_valid = verify_password(password, hashed_password)
# print("Password is valid:", is_valid)
