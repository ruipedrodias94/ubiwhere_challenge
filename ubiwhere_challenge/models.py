from flask_sqlalchemy import SQLAlchemy
from ubiwhere_challenge import db


"""
This is a test
"""

# Table user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username