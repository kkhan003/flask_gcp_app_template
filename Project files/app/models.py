from app import db
import json
# import datetime
# 'tim': int ((self.tim - datetime.datetime (1970, 1, 1)).total_seconds ()),

class Parent (db.Model):
    pid = db.Column (db.Integer, primary_key = True)
    ema = db.Column (db.String (255), nullable = False, unique = True)
    nam = db.Column (db.String (255), nullable = False)

    children = db.relationship ('Child', backref = 'parent', lazy = True, cascade = 'all, delete-orphan')

    def serialize (self):
        return {
            'pid': self.pid,
            'ema': self.ema,
            'nam': self.nam,
            'children': [ a.serialize () for a in self.children ],
        }

    def __repr__ (self):
        return '<Parent {}>'.format (self.ema)


class Child (db.Model):
    cid = db.Column (db.Integer, primary_key = True)
    nam = db.Column (db.String (255), nullable = False)

    parent_pid = db.Column(db.Integer, db.ForeignKey ('parent.pid'), nullable = False)
    
    def serialize (self):
        return {
            'cid': self.cid,
            'nam': self.nam,
        }

    def __repr__ (self):
        return '<Child {}>'.format (self.nam)