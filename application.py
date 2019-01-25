# CREDIT: KonradIT Py Library https://pypi.org/project/insight-api/

from flask import Flask, request, url_for, render_template
import json
import requests
import os

app = Flask(__name__)

@app.route('/')
def create_app():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


class InSightAPI: 
    def __init__(self, order="desc", per_page="100", af="idc"):
        self.order = order
        self.per_page = per_page
        self.af = af
        self.JSON_API = "https://mars.nasa.gov/api/v1/raw_image_items/"
        self.JSON_API += "?order=sol+" + self.order + "%2Cdate_taken+desc&per_page=" + self.per_page + "&page=PAGENUM&condition_1=insight%3Amission&search=" + self.af + "&extended="

# determining why request is needed with user_agent
def make_request(self, page_num=0):
		headers = {
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0",
			"Accept": "application/json, text/javascript, */*; q=0.01",
			"Accept-Language": "en-US,en;q=0.5",
			"X-Requested-With": "XMLHttpRequest",
			"Referer": "https://mars.nasa.gov/insight/multimedia/raw-images/?order=sol+desc%2Cdate_taken+desc&per_page=100&page=0&mission=insight&af=idc",
			"DNT": "1",
			"Connection": "keep-alive",
			"Cookie": "has_mouse=yes; raw_images_filter=order=sol+desc%2Cdate_taken+desc&per_page=100&page=" + str(page_num) + "&mission=insight&af=" + self.af + ";" +  "resources_gl_insight_multimedia_webcasts=page=0&per_page=25&order=pub_date+desc&search=&category=240%3A183&url_suffix=%3Fsite%3Dinsight; resources_gl_insight_multimedia_images=page=0&per_page=25&order=pub_date+desc&search=&category=51%3A183&fancybox=true&url_suffix=%3Fsite%3Dinsight",
			"TE": "Trailers"
		}
		response = requests.get(self.JSON_API.replace("PAGENUM",str(page_num)), headers=headers)
		return response.json()

# add event click from bootstrap template 
def get_images(self, data, num_images):
    images = []
    num_images = num_images - 1
    for i, image in enumerate(data["items"]):
        if int(i) <= num_images:
            images.append(image["url"])
    return images

def get_latest(self, data):
		return self.get_images(data, 1)