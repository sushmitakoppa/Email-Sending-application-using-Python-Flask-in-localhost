from flask_mail import Mail, Message
from flask import Flask, render_template, request

app = Flask(__name__)
mail = Mail(app)

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'YourMailidFromWhichYouCanSend@gmail.com'
app.config['MAIL_PASSWORD'] = '**********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html") #


@app.route("/submit", methods=['post'])
def sendEmail():
    emailid = request.form['email']
    msg = Message('Hello',sender = emailid,recipients=[emailid])
    msg.body = request.form['msg'] 
    mail.send(msg)
    return render_template("alert.html") #'The Message '+request.form['msg'] + ' to '+ emailid +' have been sent. '


if __name__ == '__main__':
   app.run(debug=True)
