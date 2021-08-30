from flask import Flask,session,request
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug.utils import redirect
from datetime import timedelta


app=Flask(__name__)



app.config["SECRET_KEY"]="mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config["SESSION_TYPE"]="sqlalchemy"
app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(minutes=1)
db=SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"]=db



sess=Session(app)
# db.create_all()

@app.route('/')
def index():
    if  'user' in session:
        
        print("working")
        user = session["user"]
        return render_template("index.html")
    return redirect(url_for('login'))

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        session.permanent = True
        user=request.form["nm"]
        print(user)
        print("HEKLPPPPPPPPPPPPPPP")
        session["user"]=user
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)