# built-in
import time

# core modules / packages
from core.modules import tts
from core.packages import news

"""
news
"""
def ex(cmd):
    tts.say("Suche nach Nachrichten")

    # get 5 ticks from the Google News site
    ticks = news.News.get(5)

    tts.say("Das sind die Schlagzeilen zur Stunde.")

    for title in range(5):
        tts.say(ticks[title])
        time.sleep(0.5)
