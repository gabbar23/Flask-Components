from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin,UserManager,SQLAlchemyAdapter

app=Flask(__name__)

app.config["SECRET_KEY"]="mysecret"

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///users_data.db"
app.config["CSRF_ENABLED"]=True
app.config["USER_ENABLE_EMAIL"]=False

db=SQLAlchemy(app)
class Users(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True,)
    username=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False,server_default='0')

db.create_all()
db_adapter=SQLAlchemyAdapter(db,Users)
user_manager=UserManager(db_adapter,app)



if __name__=="__main__":
    app.run(debug=True)