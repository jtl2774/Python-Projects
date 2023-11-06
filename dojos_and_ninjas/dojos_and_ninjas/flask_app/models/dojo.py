# Import MySQLConnection that will return an instance of a connection from MySQLConnection.py file in config folder
from flask_app.config.mysqlconnection import connectToMySQL
# Import Ninja class (due to table relationship)
from .ninja import Ninja

# Create new Dojo class
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # Call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    # Method to save data to db
    @classmethod
    def save(cls, data):
        # Inserts data into following fields of db
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        # Connect to name of schema in db 
        # Pass in query string above and data list
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result
    
    # Method to get ninja that belongs to a dojo
    @classmethod
    def get_one_dojo_ninja(cls,data):
        # Queries all ninjas on a Left Join to dojo table where the ninja's dojo id is equal to the dojo's id 
        query  = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        # Connect to name of schema in db 
        # Pass in query string above and data list
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        # Set variable to a result of one item in list 
        dojo = cls(result[0])
        # For each item in list retrieve the ninja's information (using for loop)
        for row in result:
            ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            # Append the Ninja data (from Ninja class) that we set as a self variable in Dojo class to a dojo 
            dojo.ninjas.append( Ninja(ninja) )
        # Rreturn the dojo variable that we set the result of each item in list to 
        return dojo
