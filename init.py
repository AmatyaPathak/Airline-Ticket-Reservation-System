from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

db = SQLAlchemy()

def createapp():
	app = Flask(__name__,	template_folder='templates', static_folder='static')
	app.config['SECRET_KEY'] = "sphinx of black quartz, judge my vow"
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
	db.init_app(app)

  
	from views import views
	from authenticate import authenticate
	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(authenticate, url_prefix='/')
  
	
	from models import Airplane, Ticket, Flight, User, Customer,BookingAgent, AirlineStaff

  
	createdatabase(app)
	login_manager = LoginManager()
	login_manager.login_view = 'authenticate.login'
	login_manager.init_app(app)
	

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))
    
	return app

def createdatabase(app):
	if(not path.exists('/database.db')):
		db.create_all(app=app)
		print("Database Created!")
