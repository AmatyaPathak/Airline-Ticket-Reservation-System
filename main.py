from flask import Flask, render_template, request, flash
from flask_login import login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from os import path
from models import *
from werkzeug.security import generate_password_hash, check_password_hash


#Initializing app and database
app = Flask(__name__)
db = SQLAlchemy()

#Secret key for website security, sqllite to be used
app.config['SECRET_KEY'] = "sphinx of black quartz, judge my vow"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
db.init_app(app)

#Create database if it doesn't already exist
if(not path.exists('/database.db')):
	db.create_all(app=app)
	print("Database Created!")

#The website routes
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

#Signup Pages
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/customersignup', methods=['GET', 'POST'])
def customersignup():
    if(request.method == 'POST'):
	    fullname = request.form.get('fullname')
	    email = request.form.get('email')
	    password1 = request.form.get('password1')
	    password2 = request.form.get('password2')
	    usertype = request.form.get('usertype')
	    user = User.query.filter_by(email=email).first()
	    if(user):
	    	flash('Account already exists, log in instead', category='error')
	    #Validating sign up form data
	    elif(len(email) < 4):
	    	flash("Invalid email, please try again", category='error')
	    elif(len(fullname) < 2):
	    	flash("Name must be greater than one character", category='error')
	    elif(len(password1) <6):
	    	flash("Password must be greater than 5 characters to be secure", category='error')
	    elif(password1 != password2):
	    	flash("Passwords don't match, please try again.", category='error')
	    else:
	    	newuser = User(fullname=fullname, email=email, password = generate_password_hash(password1, method='sha256'), usertype=usertype)
	    	db.session.add(newuser)
	    	db.session.commit()
	    	login_user(user, remember=True) 	
	    	flash("Account successfully created!", category='success')
	    	return render_template('login.html')
    return render_template('signup.html', user=current_user)


#Login Pages
@app.route('/login')
def login():
    return render_template("login.html")


if(__name__ == "__main__"):
	app.run(host='0.0.0.0',	port=5001, debug=True)