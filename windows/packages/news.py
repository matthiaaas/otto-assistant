"""
News
"""

from bs4 import BeautifulSoup
import requests


class News:
    """
    Get
    """
    def get(max_ticks):
        # the url (google news)
        url = "https://news.google.com/?hl=de&gl=DE&ceid=DE%3Ade"

        # get the source code from the url
        source_code = requests.get(url).text

        # create a bs4 object
        soup = BeautifulSoup(source_code, features="html.parser")

        # the news dict
        news = []

        class_name = "ipQwMb ekueJc RD0gLb"

        # find every item with thegiven class name
        tags = soup.find_all("h3", {"class": class_name})

        ticks = 0

        for tag in tags:
            ticks += 1
            news.append(tag.getText())
            if ticks >= max_ticks:
                break

        return news
