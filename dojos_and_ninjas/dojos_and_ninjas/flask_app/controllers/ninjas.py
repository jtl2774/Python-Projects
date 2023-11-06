# Instead of having the App Routing functions in the server.py file, we have moved them to the controllers folder. 
# We create a new py file in the pluralized form for whatever we are controlling (in this case ninjas.py) 

# Import the dependencies needed for this file
from flask import render_template,redirect,request
# Import app into flask_app
from flask_app import app
# Import dojo.py and ninja.py file in Models folder (will need both b/c of relationship b/w dojo and ninja)
from flask_app.models import dojo, ninja

# Route for new ninja page
@app.route('/ninjas')
def ninjas():    
    # Renders html that renders create ninja form
    # Call function that gets all dojos from Dojo class in dojo.py file within Models - this will be used for selecting Dojo
    # we want ninja to be placed in
    return render_template('new_ninja.html', dojos= dojo.Dojo.get_all())

# Creates new ninja & posts form data by referencing save function from models file
@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    # Calls save function from models file for ninja that allows ninja data to be saved
    ninja.Ninja.save(request.form)
    # Redirects to main Home page of Dojo 
    return redirect('/')