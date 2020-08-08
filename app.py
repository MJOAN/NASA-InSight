from flask import Flask, request, render_template, flash, g, session, redirect, url_for
from wtforms import Form, StringField, IntegerField, DateField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

from insightmars import InSightAPI, utils
InSightMission = InSightAPI()
json_request = InSightMission.make_request()

from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")

app = Flask(__name__, template_folder="templates")

class Notification(Form):
    date = DateField('date', format='%m-%d-%Y') 
    phone = IntegerField('phone', validators=[DataRequired()])
    email = StringField('email', [
        Length(min=6, message=(u'please submit a valid email address')),
        Email(message=('That\'s not a valid email address.'))
    ])
    submit = SubmitField('submit')

@app.route('/')
def create_app():
    return render_template("index.html")

@app.route('/images', methods=['GET'])
def images():
    images = InSightMission.get_all(json_request)
    # print(images, json_request)
    results = [x for x in images]
    print(results)
    return render_template("images.html", results=results)

@app.route('/sms', methods=['POST'])
def sms():
    phone = request.form['phone']
    # phone = request.args.get('phone') # use for debugging
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
                .create(
                    body="Thank you for registering to receive NASA Mars InSight Raw Image notifications! It is good to know we are going to stay in touch! Keep reaching for the planets!! :)",
                    from_=TWILIO_NUMBER,
                    to=phone
                )
    print(message.sid)
    return render_template("sms.html")

@app.route('/email', methods=['POST']) 
def email(email):
    email = request.form['email']
    return str("Thank you for registering to receive NASA Mars InSight Raw Image notifications! It is good to know we are going to stay in touch! Keep reaching for the planets! ;)")


@app.route('/metadata') # show metadata 
def metadata():
    # metadata = InSightMission.get_metadata(json_request, image_id)
    pass

if __name__ == "__main__":
    app.run(debug=True)


