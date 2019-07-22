# built-in
from datetime import datetime
import locale

# core / core modules
from assistant import settings
from assistant.core.modules import tts, replying

"""
date
says the date
"""
def ex(cmd):
    # set locale to get the right month names
    locale.setlocale(locale.LC_TIME, settings.LANGUAGE.replace("-", "_"))

    # get the date
    date = datetime.now()

    # get the day (and remove leading zero)
    day = date.strftime("%d").lstrip("0")

    # get the month name
    month = date.strftime("%B")

    # get the year
    year = date.strftime("%Y")

    tts.say(replying.get_reply("date").format(day, month, year))
