import json
import os
import urllib.request
from datetime import date

from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <a class="button" href="/list/weather/days">Weather forecast 5 days</a><br>
    <a class="button" href="/list/weather/particular">Weather on a particular date</a><br>
    """


@app.route("/list/weather/days", methods=['POST', 'GET'])
def city_weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'minsk'
    api = os.environ.get("api")
    source = urllib.request.urlopen(
        'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + api).read()
    list_of_data = json.loads(source)
    data = [
            {
                "date": str(list_of_data['list'][0]['dt_txt']),
                "temp": str(list_of_data['list'][0]['main']['temp'] - 273),
                "city": str(list_of_data['city']['name']),
                "country": str(list_of_data['city']['country'])
            },
            {
                "date": str(list_of_data['list'][7]['dt_txt']),
                "temp": str(list_of_data['list'][7]['main']['temp'] - 273),
                "city": str(list_of_data['city']['name']),
                "country": str(list_of_data['city']['country'])
            },
            {
                "date": str(list_of_data['list'][15]['dt_txt']),
                "temp": str(list_of_data['list'][15]['main']['temp'] - 273),
                "city": str(list_of_data['city']['name']),
                "country": str(list_of_data['city']['country'])
            },
            {
                "date": str(list_of_data['list'][23]['dt_txt']),
                "temp": str(list_of_data['list'][23]['main']['temp'] - 273),
                "city": str(list_of_data['city']['name']),
                "country": str(list_of_data['city']['country'])
            },
            {
                "date": str(list_of_data['list'][31]['dt_txt']),
                "temp": str(list_of_data['list'][31]['main']['temp'] - 273),
                "city": str(list_of_data['city']['name']),
                "country": str(list_of_data['city']['country'])
            },
            {
                "date": str(list_of_data['list'][39]['dt_txt']),
                "temp": str(list_of_data['list'][39]['main']['temp'] - 273),
                "city": str(list_of_data['city']['name']),
                "country": str(list_of_data['city']['country'])
            }
        ]
    print(data)
    return render_template("weather.html", data=data)


@app.route("/list/weather/particular", methods=['POST', 'GET'])
def weather_particular_date():
    if request.method == 'POST':
        date_for_api = request.form['date']
    else:
        date_for_api = str(date.today().strftime("%Y-%m-%d"))
    api_date = os.environ.get("api_date")
    weather_json = urllib.request.urlopen(
        'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/minsk,bel/' + date_for_api
        + '?key=' + api_date).read()
    list_data = json.loads(weather_json)
    data = {
        "address": str(list_data['resolvedAddress']),
        "timezone": str(list_data['timezone']),
        "datetime": str(list_data['days'][0]['datetime']),
        "temperature": str(list_data['days'][0]['temp'] - 32) + 'C',
        "conditions": str(list_data['days'][0]['conditions']),
        "description": str(list_data['days'][0]['description']),
    }
    print(data)
    return render_template("particular_date.html", data=data)


@app.route("/useragent")
def useragent():
    user_agent = request.user_agent
    return (
        '<p>your platform is: {}</p>'
        '<p>your browser is: {}</p>'.format(user_agent.platform, user_agent.browser)
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
