from app import db
from models.users import User #for ReferenceField
from models.course import COURSES

# class BMIDAILY(db.Document):
#     meta = {'collection': 'bmidaily'}
#     #store a reference field from another collection through the User object
#     #User is like a foreign key of the appUser Collection
#     user = db.ReferenceField(User)
#     date = db.DateTimeField()
#     numberOfMeasures = db.IntField()
#     averageBMI = db.FloatField()

#     def updatedBMI(self, newBMI):
#         return (newBMI + (self.averageBMI * self.numberOfMeasures)) / (self.numberOfMeasures + 1)

class BOOKINGS(db.Document):
    meta = {'collection': 'booking'}
    date = db.ListField()
    user = db.ReferenceField(User)
    courseName = db.ReferenceField(COURSES)

    
    