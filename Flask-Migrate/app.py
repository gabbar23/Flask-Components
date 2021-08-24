from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite3"
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class Create_db(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

class another_table(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
db.create_all()




if __name__=="__main__":
    app.run(debug=True)