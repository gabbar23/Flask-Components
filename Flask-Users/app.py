from enum import unique
from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin,UserManager,SQLAlchemyAdapter,current_user
from flask_mail import Mail
from flask_user.decorators import login_required

app=Flask(__name__)

app.config["SECRET_KEY"]="mysecret"

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///users_data.db"
app.config["CSRF_ENABLED"]=True
app.config["USER_ENABLE_EMAIL"]=True
app.config["USER_AFTER_REGISTER_ENDPOINT"]='user.login'
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USE_TLS"]=False
app.config["MAIL_USE_SSL"]=True
app.config["MAIL_USERNAME"]="gabbar78dummy@gmail.com"
app.config["MAIL_PASSWORD"]="yLr#06J2QvU#!1"
app.config["MAIL_DEFAULT_SENDER"]=("Message Bot","gabbar78dummy@gmail.com")


db=SQLAlchemy(app)
mail=Mail(app)
class Users(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True,)
    username=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False,server_default='')
    email=db.Column(db.String(225),unique=True,nullable=False)
    active=db.Column(db.String(20),nullable=False,server_default='0')
    confirmed_at=db.Column(db.DateTime())

db.create_all()
db_adapter=SQLAlchemyAdapter(db,Users)
user_manager=UserManager(db_adapter,app)

@app.route("/")
@login_required
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)