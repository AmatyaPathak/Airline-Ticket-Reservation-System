from flask import Blueprint, render_template
from flask_login import login_required, current_user
from init import db
from models import *
views = Blueprint('views', __name__)

@views.route('/')
def home(user):
	if(db.session.query(Customer.id).filter_by(email=user.email).first() is not None):
    return render_template('customerPortal', user=current_user)
  elif(db.session.query(AirlineStaff.id).filter_by(email=user.email).first() is not None):
    return render_template('staffPortal', user=user)
  else:
    return render_template('agentPortal', user=user)
@views.route('/customerPortal', methods=['GET', 'POST'])
def customerPortal():
  return render_template('customerPortal.html', flights=db.session.query(ticket)) 
  
  

#@views.route('/agentPortal')
'''
@views.route('/airlineStaffPortal')
def airlineStaffPortal():
	rows = AirlineStaff.query.all()
	return render_template('airlineStaffPortal.html', user=current_user, rows=rows)