"""
main.py
--------
Main entry point for the URL Shortener.
"""

from shortener import shorten_url, expand_url
from storage import get_all_urls
from utils import title


def shorten():
    """
    Shortens a URL.
    """

    url = input("\nEnter URL: ").strip()

    success, result = shorten_url(url)

    if success:
        print("\n✅ Short URL Created Successfully!")
        print(f"\nShort URL : {result}")

    else:
        print(f"\n❌ {result}")


def retrieve():
    """
    Retrieves the original URL.
    """

    short = input("\nEnter Short URL or Short Code: ").strip()

    success, result = expand_url(short)

    if success:
        print("\n🌐 Original URL")
        print(result)

    else:
        print(f"\n❌ {result}")


def view_urls():
    """
    Displays all stored URLs.
    """

    urls = get_all_urls()

    if not urls:
        print("\nNo URLs have been shortened yet.")
        return

    print("\n========== STORED URLS ==========\n")

    for index, (code, url) in enumerate(urls.items(), start=1):

        print(f"{index}.")
        print(f"Original URL : {url}")
        print(f"Short URL    : https://short.ly/{code}")
        print("-" * 50)


def menu():
    """
    Main Menu.
    """

    while True:

        title("URL SHORTENER")

        print("1. Shorten URL")
        print("2. Retrieve Original URL")
        print("3. View All URLs")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            shorten()

        elif choice == "2":
            retrieve()

        elif choice == "3":
            view_urls()

        elif choice == "4":
            print("\nThank you for using URL Shortener!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()