from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///admin.db"
app.config["SECRET_KEY"]="flask-admin"

db=SQLAlchemy(app)
admin=Admin(app,template_mode='bootstrap4')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(50))
    age = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.id)


class UserView(ModelView):
    column_exclude_list = ('password',)
    column_display_pk=True

admin.add_view(UserView(User,db.session))
admin.add_view(ModelView(Comment,db.session))


















if __name__=="__main__":
    app.run(debug=True)