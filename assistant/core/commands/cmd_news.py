# built-in
import time
import requests

from bs4 import BeautifulSoup

# core modules / packages
from assistant import settings
from assistant.core.modules import tts, replying

"""
news
"""
def ex(cmd):
    tts.say(replying.get_reply("news"))

    # check if language us German
    if settings.LANGUAGE == "de-DE":
        url = "https://news.google.com/?hl=de&gl=DE&ceid=DE%3Ade"
    # else use English
    else:
        url = "https://news.google.com/?hl=en-US&gl=US&ceid=US:en"
    
    # get the source code from the url
    source_code = requests.get(url).text
    # create a bs4 object
    soup = BeautifulSoup(source_code, features="html.parser")

    # the news dict
    news = []

    class_name = "ipQwMb ekueJc RD0gLb"
    # find every item with thegiven class name
    tags = soup.find_all("h3", {"class": class_name})

    tts.say(replying.get_reply("news", stage=1))

    ticks = 0
    # read every top title
    for tag in tags:
        ticks += 1
        title = tag.getText()
        tts.say(title)
        if ticks >= settings.MAX_NEWS_TICKS:
            break
