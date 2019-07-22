# built-in
from datetime import datetime

# core / core modules
from assistant.core.modules import tts, replying

"""
time
says the current time
"""
def ex(cmd):
    # get the date
    date = datetime.now()

    # get the time
    hour = date.strftime("%H")
    minute = date.strftime("%M")

    tts.say(replying.get_reply("time").format(hour, minute))
