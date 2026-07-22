"""
utils.py
---------
Utility functions for the URL Shortener.
"""

import random
import string
from urllib.parse import urlparse


def generate_short_code(length=6):
    """
    Generates a random short code.
    Example: A8xP2Q
    """

    characters = string.ascii_letters + string.digits

    return "".join(random.choice(characters) for _ in range(length))


def is_valid_url(url):
    """
    Checks whether the URL is valid.
    """

    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])

    except Exception:
        return False


def divider():
    print("=" * 60)


def title(text):
    divider()
    print(text.center(60))
    divider()