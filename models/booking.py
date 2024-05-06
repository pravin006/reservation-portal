# from app import db
# from models.users import User
# from models.bmilog import BMILOG

# class Booking(db.Document):
#     meta = {'collection': 'booking'}
#     user = db.ReferenceField(User)
#     courseName = db.ReferenceField(BMILOG)
#     timings = db.ListField()