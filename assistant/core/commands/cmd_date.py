# built-in
from datetime import datetime

# core / core modules
from assistant import settings
from assistant.core.modules import tts, replying

"""
date
says the date
"""
def ex(cmd):
    # imports
    from datetime import datetime

    # get the date
    day = datetime.now().strftime("%d") # day
    month = datetime.now().strftime("%m") # month
    year = datetime.now().strftime("%y") # year

    # change the month (number to word)
    months = {
        "de-DE":
            ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
        "en-US":
            ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        }
    month = months[settings.LANGUAGE][int(month)-1]

    # replace a zero with nothing
    if day.startswith("0"):
        day = day.replace("0", "")

    tts.say(replying.get_reply("date").format(day, month, year))
