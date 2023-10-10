from flask import Flask, render_template, session, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def counter():
    if 'count' in session:
        session['count']=session['count']+1
    else:
        session['count']=1   
    return render_template("index.html")

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.