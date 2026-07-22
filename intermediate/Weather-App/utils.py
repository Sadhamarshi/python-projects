"""
utils.py
---------
Utility functions for the Weather App.
"""

from datetime import datetime


def get_weather_icon(condition):
    """
    Returns an emoji based on weather condition.
    """

    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Smoke": "🌫️",
        "Haze": "🌫️",
        "Dust": "🌪️",
        "Sand": "🌪️",
        "Ash": "🌋",
        "Squall": "💨",
        "Tornado": "🌪️"
    }

    return icons.get(condition, "🌍")


def unix_to_time(timestamp):
    """
    Converts UNIX timestamp to HH:MM:SS format.
    """

    return datetime.fromtimestamp(timestamp).strftime("%I:%M:%S %p")


def current_date():
    """
    Returns current date.
    """

    return datetime.now().strftime("%d-%m-%Y")


def current_time():
    """
    Returns current time.
    """

    return datetime.now().strftime("%I:%M:%S %p")


def divider():
    """
    Prints a divider.
    """

    print("=" * 60)


def title(text):
    """
    Prints a formatted title.
    """

    divider()
    print(text.center(60))
    divider()


def format_temperature(temp, unit):
    """
    Formats temperature with unit.
    """

    if unit == "metric":
        return f"{temp:.1f} °C"

    return f"{temp:.1f} °F"


def unit_symbol(unit):
    """
    Returns the temperature symbol.
    """

    if unit == "metric":
        return "°C"

    return "°F"


def print_weather(data, unit):
    """
    Displays weather information in a clean format.
    """

    icon = get_weather_icon(data["weather"][0]["main"])

    divider()

    print(f"{icon} Weather Report")

    divider()

    print(f"City          : {data['name']}")
    print(f"Country       : {data['sys']['country']}")
    print(f"Date          : {current_date()}")
    print(f"Time          : {current_time()}")

    print()

    print(f"Condition     : {data['weather'][0]['description'].title()}")
    print(f"Temperature   : {format_temperature(data['main']['temp'], unit)}")
    print(f"Feels Like    : {format_temperature(data['main']['feels_like'], unit)}")
    print(f"Humidity      : {data['main']['humidity']}%")
    print(f"Pressure      : {data['main']['pressure']} hPa")
    print(f"Wind Speed    : {data['wind']['speed']} m/s")

    print()

    print(f"Sunrise       : {unix_to_time(data['sys']['sunrise'])}")
    print(f"Sunset        : {unix_to_time(data['sys']['sunset'])}")

    divider()