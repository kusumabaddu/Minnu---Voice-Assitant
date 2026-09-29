import webbrowser
from urllib.parse import quote


def google_search(query):

    url = (
        "https://www.google.com/search?q="
        + quote(query)
    )

    webbrowser.open(url)

    return f"Searching Google for {query}."


def youtube_search(query):

    url = (
        "https://www.youtube.com/results?search_query="
        + quote(query)
    )

    webbrowser.open(url)

    return f"Searching YouTube for {query}."


def open_website(website):

    websites = {

        "google":
            "https://www.google.com",

        "youtube":
            "https://www.youtube.com",

        "github":
            "https://github.com",

        "gmail":
            "https://mail.google.com",

    }


    if website in websites:

        webbrowser.open(
            websites[website]
        )

        return f"Opening {website}."


    return "I don't know that website."