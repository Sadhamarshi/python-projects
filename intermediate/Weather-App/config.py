"""
config.py
----------
Loads the OpenWeather API key from the .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API Key
API_KEY = os.getenv("API_KEY")

# Validate API Key
if not API_KEY:
    raise ValueError(
        "API_KEY not found. Please add your API key to the .env file."
    )

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"