from flask_login import UserMixin
from app import db

class User(UserMixin, db.Document):
    meta = {'collection': 'appUsers'}
    email = db.StringField(max_length = 30)
    password = db.StringField()
    name = db.StringField()









#USING COLLECTION
# This example is not using database. Using a dummy admn@abc.com to do a simple login

# Need to create a collection (e.g. list or dictionary) - 
# when user register, the details (email, password, name) is stored in the collection. -
# when user login, check against the collection whether usercan login or not.



#from flask_login import UserMixin
# class User(UserMixin):

#     def __init__(self):
#         self.email = 'admin@abc.com'
#         self.password = '12345'
    

#     # UserMixin class, there is this method call get_id() that we need to declare to return the id of the user for session manage

#     # e.g. set the id of the email - 
#     # this id will be used across all the python files that you need and the authentication from the front-end using Jinja 2
#     def get_id(self):
#         return self.email   # DB will have a different id - generate a unique id


#     def getEmail(self, email):
#         if email == self.email:
#             return self
#         return None
    

#     # Password