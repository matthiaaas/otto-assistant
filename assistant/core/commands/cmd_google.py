# built-in
import requests

from bs4 import BeautifulSoup

# core
from assistant import settings
# core modules packages
from assistant.core.modules import tts

"""
Google
try to find a result
from Google Search
"""
def ex(input):
    # the google search url
    key_words = input.replace(settings.KEYWORD+" ", "").lower().replace(" ", "+")
    url = "https://www.google.com/search?q={0}&hl={1}".format(key_words, settings.LANGUAGE_SHORT)

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
        text_tag = soup.find("div", {"class": "xpc"}).find("div", {"class": "BNeawe s3v9rd AP7Wnd"})
        output = text_tag.getText()

    tts.say(output)
