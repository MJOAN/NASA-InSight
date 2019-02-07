# reference konradIT py library https://pypi.org/project/insight-api/
from flask import Flask, request, render_template, flash, g, session, redirect, url_for
from wtforms import Form, StringField, DateField, SubmitField, PhoneNumberField, validators
from wtforms_components import Email, PhoneNumberField
import requests
import json


app = Flask(__name__, template_folder="templates")

class ImageForm(Form):
    date = DateField('date', format='%m-%d-%Y')
    email = TextField('email', [validators.Length(min=6, max=35), validators=[Email()])
    phone = PhoneNumberField('phone', validators=[country_code='FI', display_format='national'])
    submit = SubmitField('submit')

# "2014-12-10T16:44:31.486000Z"
# date format = "yyyy-MM-dd'T'HH:mm:ss.SZ"
# image = print(date["items"][0]["url"])
# date = print(date["items"][0]["date_taken"] 
# TODO: parse date user input 

@app.route('/')
def create_app():
    return render_template("index.html")

@app.route('/get_images', methods=['GET'])
def get_images(self, date):
    date = request.form['date']
    if date.validate_on_submit():
        images = []
        for i, image in enumerate(date["items"]):
            if int(i) <= 10:
                images.append(image["url"])
        return images


@app.route('/get_notification', methods=['POST']) # from date params
def get_notification(self, email, phone):
    email = request.form['email']
    phone = request.form['phone']


    pass

@app.route('/image/metadata') # show metadata 
def get_metadata(self, metadata):
    pass


if __name__ == "__main__":
    app.run(debug=True)