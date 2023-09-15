from init import db
from flask_login import UserMixin
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

class Airport(db.Model):
  name = db.Column(db.String(40), primary_key=True)

class Airline(db.Model):
  name = db.Column(db.String(40), primary_key=True)

class Airplane(db.Model):
  id = db.Column(db.Integer, primary_key = True)

class Ticket(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(1000))
  date = db.Column(db.DateTime(timezone=True), default = datetime.utcnow())
  userid = db.Column(db.Integer, db.ForeignKey('user.id'))
  price = db.Column(db.Integer)
  
class Flight(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  plane_id = db.Column('plane_id', db.Integer, db.ForeignKey('airplane.id'))
  airline = db.Column('airline', db.Integer, db.ForeignKey('airline.name'))
  origin = db.Column('origin_airport', db.String(40), db.ForeignKey('airport.name'))
  destinataion = db.Column('dest_airport', db.String(40), db.ForeignKey('airport.name'))
  departure_time = db.Column(db.DateTime())
  arrival_time = db.Column(db.DateTime())
  price = db.Column('price', db.Integer, db.ForeignKey('ticket.price'))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  dob = db.Column(db.Date())

class Customer(User):
  tickets = db.Column(db.String(100))


class BookingAgent(User):
	agent_id = db.Column(db.Integer)

class Airlinestaff(User):	
  phonenumber = db.Column(db.Integer)
  



owns = db.Table('owns', 
  db.Column('airline_name', db.String(40)), 
  db.Column('plane_id', db.Integer, db.ForeignKey('airplane.id')))

'''
worksAt = db.Table('worksAt',
  db.Column('airline_name', db.String(40), db.ForeignKey('airline.name')),
  db.Column('airlineStaff_email', db.String(40), db.ForeignKey('airlinestaff.email')))

organizes = db.Table('organizes', 
  db.Column('flight', db.Integer, db.ForeignKey('flight.id')),
  db.Column('organizer', db.String(40), db.ForeignKey('airline.name')))

departures = db.Table('departures',
  db.Column('flight', db.Integer, db.ForeignKey('flight.id')),
  db.Column('airport', db.String(40), db.ForeignKey('airport.name')))

arrivals = db.Table('arrivals',
  db.Column('flight', db.Integer, db.ForeignKey('flight.id')),
  db.Column('airport', db.String(40), db.ForeignKey('airport.name')))

purchases = db.Table('purchases',
  db.Column('customer', db.Integer, db.ForeignKey('customer.id')),
  db.Column('ticket', db.Integer, db.ForeignKey('ticket.id')),
  db.Column('agent', db.Integer, db.ForeignKey('agent.agent_id')))

'''