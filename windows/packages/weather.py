"""
Weather
"""

from bs4 import BeautifulSoup
import requests


class Weather:
    """
    Lookup
    """
    def lookup(location):
        # the url
        location.lower().replace(" ", "+")
        url = "https://www.wetteronline.de/wettertrend/"+location

        # get the source code from the url
        source_code = requests.get(url).text
        # create a bs4 object
        soup = BeautifulSoup(source_code, features="html.parser")

        # get the short weather description
        text_tag = soup.find("div", {"data-day": "today"})

        return text_tag.getText()


    """
    Forecast
    """
    def forecast(location):
        # the url
        location.lower().replace(" ", "+")
        url = "https://www.wetteronline.de/wettertrend/"+location

        # get the source code from the url
        source_code = requests.get(url).text
        # create a bs4 object
        soup = BeautifulSoup(source_code, features="html.parser")

        # get the short weather description
        text_tag = soup.find("div", {"data-day": "tomorrow"})

        return text_tag.getText()
