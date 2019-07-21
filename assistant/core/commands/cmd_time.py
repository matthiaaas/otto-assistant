# built-in
from datetime import datetime

# core / core modules
from assistant.core.modules import tts, replying

"""
time
says the current time
"""
def ex(cmd):
    # get the time
    uhrzeit = datetime.now().strftime("%H:%M")

    # make the time ready to read
    h = uhrzeit.split(":")[0]
    m = uhrzeit.split(":")[1]

    tts.say(replying.get_reply("time").format(h, m))
