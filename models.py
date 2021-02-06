from flask_sqlalchemy import SQLAlchemy 

db=SQLAlchemy()
mydb="postgres://saad:1234@localhost/mydb"

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    number=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)
    
class MakeFriend(db.Model):
    __tablename__="friends"
    id=db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Integer, db.ForeignKey("users.id"))
    friendid=db.Column(db.Integer, nullable=False)
    