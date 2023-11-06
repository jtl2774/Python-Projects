# Instead of having the App Routing functions in the server.py file, we have moved them to the controllers folder. 
# We create a new py file in the pluralized form for whatever we are controlling (in this case dojos.py)

# Import the dependencies needed for this file
from flask import render_template,redirect,request
# Import app into flask_app
from flask_app import app
# Import Dojo class from dojo.py file in Models folder
from flask_app.models.dojo import Dojo

# The following are App Routing 'functions'. The app.route decorator is used to bind a function a URL path. 
# When we type this URL path into our browser, we should be brought to the page that renders the HTML template
# we have linked the route to.   

@app.route('/')
def first():
    return redirect('/dojos')

# Returns all dojos from the database
@app.route("/dojos")
def index():
    # call the get all classmethod to get all dojos
    dojo = Dojo.get_all()
    # Renders html that displays list of all users, set dojo variable that was just created to all_dojos
    return render_template("dojo.html", all_dojos = dojo)

# Creates new dojo & posts form data by referencing save function from models file 
@app.route('/dojo/create', methods=['POST'])
def create():
    # Save function from models file - saves to database 
    Dojo.save(request.form)
    # Redirects to main all dojo list page once create button is clicked
    return redirect('/dojos')

# Shows more information about a dojo and the ninjas within a dojo using each dojo id
@app.route("/show/dojo/<int:id>")
def show_dojo_ninja(id):
    # Create data object for id
    data ={ 
        "id":id
    }
    # Renders HTML template that shows info about dojo and gets each ninja that belongs to dojo data for that one dojo by passing in data object 
    # Calls function from dojo.py in Models folder to retrieve data
    return render_template("dojo_ninjas.html",dojo= Dojo.get_one_dojo_ninja(data))
