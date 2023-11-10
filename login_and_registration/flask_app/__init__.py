# Import flask 
from flask import Flask
# Set up app
app = Flask(__name__)
# Create secret key used to sign session cookies for protection against cookie data tampering
app.secret_key = "Mysterious wonders that thou shalln't know"