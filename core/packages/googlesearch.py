"""
googlesearch.py
A program that searches for
keywords using Google Search
and returns a short text if
succesful.
"""

import requests

from bs4 import BeautifulSoup


# Search
class Search:
    """
    Returns a small preview
    text from Google Search.
    """
    def get(key_words):
        # the google search url
        key_words.lower().replace(" ", "+")
        url = "https://www.google.com/search?q="+key_words

        # get the source code from the url
        source_code = requests.get(url).text

        # create a bs4 object
        soup = BeautifulSoup(source_code, features="html.parser")

        # try to find a short answer
        try:
            text_tag = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
            output = text_tag.getText()

        # get a longer text
        except:
            text_tag = soup.find("div", {"class": "BNeawe s3v9rd AP7Wnd"})
            output = text_tag.getText()

        return output
