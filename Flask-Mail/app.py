from flask import Flask
from flask_mail import Mail,Message

app=Flask(__name__)
#MAIL_CONFIGRATION

app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USE_TLS"]=False
app.config["MAIL_USE_SSL"]=True
app.config["MAIL_USERNAME"]="gabbar78dummy@gmail.com"
app.config["MAIL_PASSWORD"]="yLr#06J2QvU#!1"
app.config["MAIL_DEFAULT_SENDER"]=("Message Bot","gabbar78dummy@gmail.com")
mail=Mail()
mail.init_app(app)

@app.route('/')
def index():
    msg=Message(subject="FlaskTest",body="Yo SUPPP1111PPPP",recipients=["amansaini842@gmail.com"])
    with app.open_resource("Synonyms_with_Vocabs.pdf") as pdf:
        msg.attach("Synoms",'application/pdf',pdf.read())
    mail.send(msg)
    return "Sent"

if __name__=="__main__":
    app.run(debug=True)