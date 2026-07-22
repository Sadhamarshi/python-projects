"""
storage.py
-----------
Handles saving and loading URL data using a JSON file.
"""

import json
import os

FILE_NAME = "urls.json"


def create_storage():
    """
    Creates urls.json if it doesn't exist.
    """

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)


def load_urls():
    """
    Loads all saved URLs.

    Returns:
        dict
    """

    create_storage()

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, dict):
                return data

            return {}

    except json.JSONDecodeError:
        return {}

    except Exception:
        return {}


def save_urls(data):
    """
    Saves the URL dictionary to urls.json.

    Parameters:
        data (dict)
    """

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def add_url(short_code, original_url):
    """
    Adds a new URL mapping.
    """

    data = load_urls()

    data[short_code] = original_url

    save_urls(data)


def get_original_url(short_code):
    """
    Returns the original URL for a given short code.

    Returns:
        str or None
    """

    data = load_urls()

    return data.get(short_code)


def url_exists(original_url):
    """
    Checks whether the URL has already been shortened.

    Returns:
        Existing short code or None.
    """

    data = load_urls()

    for code, url in data.items():

        if url == original_url:
            return code

    return None


def short_code_exists(short_code):
    """
    Checks whether a short code already exists.
    """

    data = load_urls()

    return short_code in data


def get_all_urls():
    """
    Returns every saved URL.
    """

    return load_urls()