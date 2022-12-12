# code review by
from flask import Flask, request, render_template, send_from_directory
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open("index.html", "r") as content:
        page = content.read()
    return page


@app.route('/doron')
def index1():
    return '''<img src="https://media.npr.org/assets/img/2017/09/12/macaca_nigra_self-portrait-3e0070aa19a7fe36e802253048411a38f14a79f8-s800-c85.webp">'''


def get_weather(location):
    print(f"user input {location}")
    api_key = "MWZH3TF724T3B2LW67JPNAD55"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next7days?unitGroup=metric&elements=datetime%2Ctempmax%2Ctempmin%2Ctemp%2Chumidity%2Cicon&include=days%2Cfcst&key={api_key}&options=nonulls&contentType=json"
    try:
        response = requests.get(url).json()
        print("api response", response)
        return response
    except:
        print("Error")
        return None


@app.route('/loc', methods=['POST'])
def weather():
    if request.method == 'POST':
        local = request.form['location']
        print(local)
        res = get_weather(local)
        if res is None:
            return render_template("error.html")
        return render_template("weather.html", res=res, loc=local)


app.run(host="0.0.0.0",port=5000)
