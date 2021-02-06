from flask import *
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=mydb
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

with app.app_context():
    db.create_all()
    