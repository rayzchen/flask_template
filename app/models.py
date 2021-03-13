from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(27), primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    first_name = db.Column(db.String(20), index=True, unique=True)
    last_name = db.Column(db.String(20), index=True, unique=True)
    age = db.Column(db.Integer, index=True, unique=True)