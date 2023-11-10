# Import app since server is still being run as main entry point 
from flask_app import app
# Because we moved all the App Route functions to the controllers folder we need to import those files to server.py now
from flask_app.controllers import users

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.