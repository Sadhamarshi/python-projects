"""
weather.py
-----------
Handles communication with the OpenWeather API.
"""

import requests
from config import API_KEY, BASE_URL


def get_weather(city, unit="metric"):
    """
    Fetches current weather data for the given city.

    Parameters:
        city (str): Name of the city.
        unit (str): "metric" for Celsius or "imperial" for Fahrenheit.

    Returns:
        tuple:
            (True, weather_data) on success
            (False, error_message) on failure
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": unit
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Successful request
        if response.status_code == 200:
            return True, response.json()

        # Invalid city
        elif response.status_code == 404:
            return False, "City not found."

        # Invalid API Key
        elif response.status_code == 401:
            return False, "Invalid API Key."

        # Other API errors
        else:
            return False, f"API Error ({response.status_code})"

    except requests.exceptions.Timeout:
        return False, "Request timed out."

    except requests.exceptions.ConnectionError:
        return False, "No internet connection."

    except requests.exceptions.RequestException as error:
        return False, f"Request Error: {error}"

    except Exception as error:
        return False, f"Unexpected Error: {error}"