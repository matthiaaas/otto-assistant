# built-in
from datetime import datetime

# core / core modules
from core.modules import tts

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
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    month = months[int(month)-1]

    # replace a zero with nothing
    if day.startswith("0"):
        day = day.replace("0", "")

    tts.say("Heute ist der {0}te {1} 20{2}".format(day, month, year))
