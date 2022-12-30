#! /usr/bin/python3
'''microservice to return timzone information based on a city'''
from flask import Flask, jsonify
from gettimezone import get_time_in_timezone

app = Flask(__name__)
# Define the cities and timezones
cities = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo"
}

@app.route('/time/<city>')
def get_time(city):
    if city not in cities:
        return "Invalid city", 400
    
    timezone = cities[city]
    time = get_time_in_timezone(city, timezone)
    
    return jsonify({ "time": time })

if __name__ == '__main__':
    app.run()
