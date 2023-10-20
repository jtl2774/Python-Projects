# Instead of having the App Routing functions in the server.py file, we have moved them to the controllers folder. 
# We create a new py file in the pluralized form for whatever we are controlling (in this case users.py)

# Import the dependencies needed for this file
from flask import render_template,redirect,request
# Import app into flask_app
from flask_app import app
# Import user class from user.py file in Models folder
from flask_app.models.user import User


# The following are App Routing 'functions'. The app.route decorator is used to bind a function a URL path. 
# When we type this URL path into our browser, we should be brought to the page that renders the HTML template
# we have linked the route to.  

# Returns all users from the database
@app.route("/users")
def all_user():
    # Renders html that displays list of all users and retrieves all users from User class get_all()
    return render_template("user.html", user = User.get_all())

# Renders html template for creating new user
@app.route("/new/user")
def new_user():
    return render_template("new_user.html")

# Creates new user & posts form data by referencing save function from models file 
@app.route('/user/create', methods=['POST'])
def create():
    if not User.validate_user(request.form):
        return redirect("/")
    # Save function from models file - saves to database 
    User.save(request.form)
    # Redirects to main all user list page once create button is clicked
    return redirect('/users')

# Edit ability for one user 
@app.route('/user/edit/<int:id>')
# Pass in id to reference the user id we will need 
def edit_user(id):
    # Create data object for id
    data ={ 
        "id":id
    }
    # Renders edit html page and gets the user data for that one user by passing in data object
    return render_template("user_edit.html", user=User.get_one(data))

# Shows more information about a user
@app.route('/user/show/<int:id>')
def show(id):
    # Create data object for id
    data ={ 
        "id":id
    }
    # Renders page that shows info about user and gets the user data for that one user by passing in data object 
    return render_template("show_user.html",user=User.get_one(data))

# Updates information about a user and posts form data 
@app.route('/user/update', methods=['POST'])
def update():
    # Calls update function from User class in models folder
    User.update(request.form)
    # Redirects to main all user list page once update button is clicked
    return redirect('/users')

# Deletes a user from the database 
@app.route('/user/destroy/<int:id>')
def destroy(id):
    # Create data object for id
    data ={
        'id': id
    }
    # Calls delete(destroy) function from User class in models folder by passing in data object 
    User.destroy(data)
    # Redirects to main all user list page once update button is clicked
    return redirect('/users')
