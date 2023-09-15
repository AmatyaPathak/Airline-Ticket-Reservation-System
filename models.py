from main import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  dob = db.Column(db.Date())