# built-in
import json
import requests

# core
from assistant import settings
# core modules / packages
from assistant.core.modules import log, tts, replying

"""
weather
says the todays'
weather
"""
def ex(cmd):
    # weather request url
    url = "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&lang={2}&units=metric".format(settings.LOCATION, settings.WEATHER_API_KEY, settings.LANGUAGE_SHORT)

    # get the source code from the url
    data = requests.get(url)
    # convert json
    content = json.loads(data.text)

    # get data
    # test if there's an error message
    if "message" in content:
        log.error(content["message"])
        tts.say(content["message"])
    # get real data
    else:
        temp = content["main"]["temp"]
        temp_max = content["main"]["temp_max"]
        desc = content["weather"][0]["description"]

        tts.say(replying.get_reply("weather").format(settings.LOCATION, temp, desc, temp_max))
