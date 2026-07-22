"""
shortener.py
------------
Core logic for the URL Shortener.
"""

from utils import generate_short_code, is_valid_url
from storage import (
    add_url,
    get_original_url,
    url_exists,
    short_code_exists
)

BASE_URL = "https://short.ly/"


def shorten_url(original_url):
    """
    Shortens the given URL.

    Parameters:
        original_url (str)

    Returns:
        tuple:
            (True, short_url)
            (False, error_message)
    """

    # Validate URL
    if not is_valid_url(original_url):
        return False, "Invalid URL. Please include http:// or https://"

    # Check if URL already exists
    existing_code = url_exists(original_url)

    if existing_code:
        return True, BASE_URL + existing_code

    # Generate a unique short code
    while True:

        short_code = generate_short_code()

        if not short_code_exists(short_code):
            break

    # Save URL
    add_url(short_code, original_url)

    return True, BASE_URL + short_code


def expand_url(short_code):
    """
    Retrieves the original URL.

    Parameters:
        short_code (str)

    Returns:
        tuple:
            (True, original_url)
            (False, error_message)
    """

    short_code = short_code.strip()

    if short_code.startswith(BASE_URL):
        short_code = short_code.replace(BASE_URL, "")

    original_url = get_original_url(short_code)

    if original_url:
        return True, original_url

    return False, "Short URL not found."


def get_short_code(short_url):
    """
    Extracts the short code from a short URL.
    """

    if short_url.startswith(BASE_URL):
        return short_url.replace(BASE_URL, "")

    return short_url