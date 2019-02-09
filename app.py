from flask import Flask, request, render_template, flash, g, session, redirect, url_for
from wtforms import Form, StringField, IntegerField, DateField, SubmitField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

from insightmars import InSightAPI, utils
InSightMission = InSightAPI()
json_request = InSightMission.make_request()

from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib

import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
accounts_id = os.getenv('TWILIO_ACCOUNT_SID')
account_token = os.getenv('TWILIO_AUTH_TOKEN')
account_sid = accounts_id
auth_token = account_token

app = Flask(__name__, template_folder="templates")

class Notification(Form):
    date = DateField('date', format='%m-%d-%Y') 
    phone = IntegerField('phone')
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


@app.route('/sms', methods=['POST']) # from date params
def sms(phone):
    phone = request.form['phone']
    client = Client('TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN')
    # message = MessagingResponse()
    message = client.messages \
                .create(
                    body="Thank you for registering to receive NASA Mars InSight Raw Image notifications! It is good to know we are going to stay in touch! Keep reaching for the planets!! :)",
                    from_='+12139557528',
                    to=phone
                )
    print(message.sid)
    return str(message)

@app.route('/email', methods=['POST']) # from date params
def email(email):
    email = request.form['email']
    return str("Thank you for registering to receive NASA Mars InSight Raw Image notifications! It is good to know we are going to stay in touch! Keep reaching for the planets! ;)")


@app.route('/metadata') # show metadata 
def metadata():
    # metadata = InSightMission.get_metadata(json_request, image_id)
    pass


if __name__ == "__main__":
    app.run(debug=True)


