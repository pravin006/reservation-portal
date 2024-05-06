from app import db
from models.holes import HOLE


class COURSES(db.Document):
    meta = {'collection': 'course'}
    course = db.StringField()
    
    holes = db.ListField(db.ReferenceField(HOLE))
    image_url = db.StringField()
    description = db.StringField()