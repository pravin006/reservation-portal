from flask import Flask

from flask_login import LoginManager

from flask_mongoengine import MongoEngine, Document

def create_app():
    #Congig for app
    app = Flask(__name__)

    # This line of code is to the assets folder where we store our HTML, CSS and JS files
    app.static_folder = 'assets'

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

    #Config for login
    # The most important part of an application that uses Flask-Login is the LoginManager class. 
    login_manager = LoginManager() #login manager expects a login page

    # Once the actual application object has been created, you can configure it for login with:
    login_manager.init_app(app)


    # By default, when a user attempts to access a login_required view without being logged in, 
    # Flask-Login will flash a message and redirect them to the log in view. 

    # The name of the log in view can be set as LoginManager.login_view.
    login_manager.login_view = 'auth.login' #if login view is not created, 404 error is shown in browser

    #initialize database using mongoengine
    app.config['MONGODB_SETTINGS'] = {
        'db':'golf',
        'host':'localhost'
    }
    db = MongoEngine(app)

    return app, login_manager, db


app, login_manager, db = create_app()



