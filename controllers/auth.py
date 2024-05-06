from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash # for hashing and reading hashed password

from models.forms import RegForm
from models.users import User


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            #check if user exists in database
            #find the first document that has the email from database(email=form.email.data.first()). email is unique, should only  have the one
            # convert the document into an object using .objects()
            # existing_user is an User() object or None
            existing_user = User.objects(email=form.email.data).first()

            if existing_user is None:
                #store the User into db
                #hash the password
                hashpass = generate_password_hash(form.password.data,method= 'pbkdf2:sha256')
                #create the User object and save to db using .save() method from mongoengine
                hey = User(email=form.email.data,password=hashpass,name=form.name.data).save()

                #after saved User to db, login the user
                login_user(hey)
                return redirect( url_for('courses.render_courses') )
            else:
                form.email.errors.append("User already existed")
          
    return render_template('register.html', form=form, panel="Register")



@auth.route('/login', methods=['GET', 'POST'])
@auth.route('/')
def login():
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            #get the user object from db. can be obj or None
            check_user = User.objects(email=form.email.data).first()
            if check_user:
                #read the hashed password from the User object against the pawssword input in the form
                if check_password_hash(check_user['password'], form.password.data):
                    login_user(check_user)
                    return redirect(url_for('courses.render_courses'))
                else:
                    form.password.errors.append("User Password Not Correct")
            else:
                form.email.errors.append("No Such User")


    return render_template('login.html', form=form, panel="Login")
        #     print ("Check name and password with database - Cover in Seminar 4")
            # Example: if user password not correct to check from a dictionary or in database

            # Need to check database

            # Just check a dummy user admin@abc.com in our User Class, did not check the password
            # getUser = User()

            # check_user = getUser.getEmail(form.email.data)


            # if check_user:
            #     # From the flask_login package to login a user and create a session 
            #     login_user(check_user)      # check_user is a User object 
            #     return redirect( url_for('dashboard.render_dashboard') )

            # else:
            #     form.email.errors.append("User Email Not Correct")

    # flash('You are at the login page now. Hello World')

    # return render_template('login.html', form=form, panel="Login")



@auth.route('/logout', methods = ['GET'])
@login_required
def logout():

    # From the flask-login package to logout a user and stop a session
    logout_user()
    return redirect(url_for('auth.login'))


