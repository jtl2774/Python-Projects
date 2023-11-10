# Instead of having the App Routing functions in the server.py file, we have moved them to the controllers folder. 
# We create a new py file in the pluralized form for the object we are controlling (in this case users.py) 

# Import the dependencies needed for this file
from flask import render_template,redirect,request,session
# Import app into flask_app
from flask_app import app
# Import User class from user file in Models folder
from flask_app.models.user import User
# we are creating an object called bcrypt,  
# which is made by invoking the function Bcrypt with our app as an argument
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# Import flash
from flask import flash

# Root route that displays template for login and registration forms 
@app.route("/")
def index():
    return render_template("index.html")

# Root route for when user submits registration form 
@app.route("/register", methods=['POST'])
def register():
    # if there are errors:
    # We call the staticmethod on User model to validate
    if not User.validate_user(request.form):
        # redirect to the route where the user form is rendered
        return redirect('/')
    # Create the hash
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    # else no errors: 
    # User.save(request.form) # Save data using save method from User model
    return redirect("/welcome") # Redirect to dashboard page

# Root route for when user logins
@app.route('/login', methods=['POST'])
def login():
    # see if the user provided exists 
    data = { "email" : request.form["email"] }
    user = User.get_user_by_email(data)
    # if user is not registered 
    if not user:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user.id
    # never render template on a post!!!
    return redirect("/welcome")

# Root route for main welcome screen after logging in
@app.route("/welcome")
def dashboard():
    # Checks to see if user_id is stored in session 
    if 'user_id' not in session:
        return redirect("/logout")
    return render_template("welcome.html")

# Root route for logging out
@app.route("/logout")
def logout():
    # clear session once logout
    session.clear()
    # redirect to home page
    return redirect("/")
