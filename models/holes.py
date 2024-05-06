from app import db

class HOLE(db.Document):
    meta = {'collection': 'holes'}
    index = db.IntField()
    par = db.IntField()
    dist = db.IntField()