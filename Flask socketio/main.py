from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO, emit,send

app=Flask(__name__)
app.config["SECRET_KEY"]="secret"
app.config["DEBUG"]=True

socketio=SocketIO(app)


@app.route('/')
def index():
    return render_template("index.html")

# @socketio.on('message')
# def recieve_fucntion(message):
#     print("######{}".format(message))
#     send("hiiii")

# @socketio.on('custom event')
# def recieve_custom_event(message):
#     print(message)
#     emit('from flask',{"hi":"lol"})

@socketio.on('message from the user')
def recieve_custom_event(message):
    print(message)
    

if __name__=="__main__":
    socketio.run(app)
