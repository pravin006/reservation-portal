from flask import Flask, render_template, request, jsonify, Blueprint
from app import app, login_manager, db

from models.users import User


from controllers.auth import auth
app.register_blueprint(auth)


from controllers.dashboard import dashboard
app.register_blueprint(dashboard)

from controllers.courses import courses
app.register_blueprint(courses)

from controllers.booking import booking
app.register_blueprint(booking)

from controllers.selectdt import selectdt
app.register_blueprint(selectdt)

from controllers.chartdashboard import chartdashboard
app.register_blueprint(chartdashboard)

from controllers.upload import upload
app.register_blueprint(upload)

from flask_login import current_user

# Load the current user if any (if user login, make use of the user id to get the email.) 
# You will need to provide a user_loader callback. 
# This callback is used to reload the user object from the user ID stored in the session. 
@login_manager.user_loader
def load_user(user_id):
    #return the User object with primary key = email thats was passed in with obj
    return User.objects(pk = user_id).first() #pk means primary key
