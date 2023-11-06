# Import MySQLConnection that will return an instance of a connection from MySQLConnection.py file in config folder
from flask_app.config.mysqlconnection import connectToMySQL

# Create new Ninja class
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Function for saving Ninja data into db
    @classmethod
    def save(cls, data):
        # Inserts data into following fields of db
        query = "INSERT INTO ninjas (first_name,last_name,age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        # Connect to name of schema in db 
        # Pass in query string above and data list
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result
