#! /usr/bin/python3
'''Get the time in a timezone'''

import pytz
from datetime import datetime

def get_time_in_timezone(city, timezone):
    # Get the timezone object for the given city and timezone
    tz = pytz.timezone(timezone)
    
    # Get the current time in the specified timezone
    time = datetime.now(tz)
    
    # Return the time as a formatted string
    return time.strftime("%H:%M:%S")

# Define the cities and timezones
cities = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo"
}

# Iterate over the cities and print the time for each one
for city, timezone in cities.items():
    print(f"The time in {city} is {get_time_in_timezone(city, timezone)}")
