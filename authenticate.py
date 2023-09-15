from flask import Blueprint, render_template, request, flash
from models import User
from init import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

authenticate = Blueprint('authenticate', __name__)

@authenticate.route('/login', methods=['GET', 'POST'])
def login():
	if(request.method == 'POST'):
		email = request.form.get('email')
		password = request.form.get('password1')
		user = User.query.filter_by(email=email).first()
		usertype = request.form.get('usertype')
		print(user)
		if(user): 
			if(check_password_hash(user.password, password) and user.usertype == usertype):
				flash('Logged in successfully!', category='success')
				login_user(user, remember=True)
				return render_template('home.html', user=current_user)
			else:
				flash('Incorrect password, please try again', category='error')
		else:
			flash('No associated account with that email, sign up instead', category='error')
	return render_template('login.html', user=current_user)

@authenticate.route('/logout')
def logout():
	logout_user()
	flash('Logged out successfully!', category='success')
	return render_template('login.html', user=current_user)

@authenticate.route('/signup', methods=['GET', 'POST'])
def signup():
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
			return render_template('home.html')
	return render_template('signup.html', user=current_user)