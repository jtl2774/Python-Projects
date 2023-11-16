# Import flask
from flask import Flask
from flask_bcrypt import Bcrypt
# Set up app
app = Flask(__name__)
# Create an object called bcrypt,  
# which is made by invoking the function Bcrypt with our app as an argument
bcrypt = Bcrypt(app)
# Create secret key used to sign session cookies for protection against cookie data tampering
app.secret_key="Shh don't tell"