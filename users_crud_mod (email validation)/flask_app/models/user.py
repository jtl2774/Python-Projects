# Import MySQLConnection that will return an instance of a connection from MySQLConnection.py file in config folder
from flask_app.config.mysqlconnection import connectToMySQL
# Import flash component into app 
from flask import flash 
import re	# the regex module
# create a regular expression object that we'll use later for email validation  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# Create new User class 
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod 
    def get_all(cls):
        # Queries all users from db
        query = "SELECT * FROM users;"
        # Call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_one(cls,data):
        # Selects one user from db based on id
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        # Connect to name of schema in db 
        # Pass in query string above and data list
        result = connectToMySQL('users').query_db(query,data)
        # return result of one item in list 
        return cls(result[0])
    
    
    @classmethod
    def save(cls, data):
        # Inserts data into following fields of db
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        # Connect to name of schema in db 
        # Pass in query string above and data list
        result = connectToMySQL('users').query_db(query,data)
        # returns result
        return result
    
    @classmethod
    def update(cls,data):
        # Updates fields about a user in db
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
        # Connect to schema in db
        # Pass in query string above and data list
        return connectToMySQL('users').query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        # Deletes user from db based on id
        query  = "DELETE FROM users WHERE id = %(id)s;"
        # Connect to name of schema in db 
        # Pass in query string above and data list
        return connectToMySQL('users').query_db(query,data)
    
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
        if len(user['first_name']) < 0:
            # Flash message to display if characters are less than 2, category for message set to 'register'
            flash("First Name is required.")
            # Sets is_valid variable to false
            is_valid = False
        #  Last Name: letters only, at least 2 characters and that it was submitted
        if len(user['last_name']) < 0:
            # Flash message to display if characters are less than 2, category for message set to 'register'
            flash("Last Name is required.")
            is_valid = False
        if len(user['email']) < 0:
            # Flash message to display if characters are less than 2, category for message set to 'register'
            flash("Email is required.")
            is_valid = False
        # Test whether email field matches the regex pattern set above
        if not EMAIL_REGEX.match(user['email']):
            # Sends invalid message if email is invalid, category for message set to 'register'
            flash("Invalid Email format.")
            # Sets is_valid variable to false
            is_valid = False
        return is_valid