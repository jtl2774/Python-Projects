# Import MySQLConnection that will return an instance of a connection from MySQLConnection.py file in config folder
from flask_app.config.mysqlconnection import connectToMySQL
# Import flash component into app 
from flask import flash 
import re	# the regex module
# create a regular expression object that we'll use later for email validation  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# Create new instance of User class
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Method to save data to db
    @classmethod
    def save(cls, data):
        # Inserts data into following fields of db
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        # Connect to name of schema in db and pass in query string above/data list
        return connectToMySQL('registration_users').query_db(query,data)
    
    # Method to get a user by email address 
    @classmethod
    def get_user_by_email(cls, data):
        # Retrieves email from db 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        # Connect to name of schema in db and pass in query string above/data list
        result = connectToMySQL('registration_users').query_db(query,data)
        # Checks to see if email exists by checking length 
        if len(result) < 1:
            return False
        # If email exists return a email in the email list
        return cls(result[0])
    
    # Method to validate registration inputs
    @staticmethod
    def validate_user(user):
        is_valid = True # Assume this is true initially
        # Retrieve email field from users table 
        query = "SELECT * FROM users WHERE email = %(email)s;" 
        # Connect to name of schema in db 
        # Pass in query string above and data list
        result = connectToMySQL('registration_users').query_db(query,user)
        # Create validation for the following fields
        # First Name:  letters only, at least 2 characters and that it was submitted
        if len(user['first_name']) < 2:
            # Flash message to display if characters are less than 2, category for message set to 'register'
            flash("First Name must be at least 2 characters.", "register")
            # Sets is_valid variable to false
            is_valid = False
        #  Last Name: letters only, at least 2 characters and that it was submitted
        if len(user['last_name']) < 3:
            # Flash message to display if characters are less than 2, category for message set to 'register'
            flash("Last Name must be at least 2 characters.", "register")
            is_valid = False
        # Email: valid Email format, does not already exist in the database, and that it was submitted
        # Checks to see if results queried from db already exists, a length greater than or equal to one
            # indicates that there is an email alreay populated in that field
        if len(result) >= 1:
            # If already exists sends following flash message, category for message set to 'register'
            flash("Email already taken.","register")
            # Sets is_valid variable to false
            is_valid = False
        # Test whether email field matches the regex pattern set above
        if not EMAIL_REGEX.match(user['email']):
            # Sends invalid message if email is invalid, category for message set to 'register'
            flash("Invalid Email!!!","register")
            # Sets is_valid variable to false
            is_valid = False
        # Password:  at least 8 characters, and that it was submitted
        if len(user['password']) < 8:
            # Flash message to display if characters are less than 8, category for message set to 'register'
            flash("Password must be at least 8 characters","register")
            # Sets is_valid variable to false
            is_valid = False
        # Password Confirmation: matches password 
        if user['password'] != user['password_confirmation']:
            # Flash message to display if passwords don't match, category for message set to 'register'
            flash("Passwords don't match","register")
            # Sets is_valid variable to false
            is_valid = False
        return is_valid
