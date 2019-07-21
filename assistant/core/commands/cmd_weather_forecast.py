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
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&appid={1}&lang={2}&units=metric&cnt=1".format(settings.LOCATION, settings.WEATHER_API_KEY, settings.LANGUAGE_SHORT)

    # get the source code from the url
    data = requests.get(url)
    # convert json
    content = json.loads(data.text)

    # get data
    try:
        # test if there's an error message
        log.error(content["message"])
    except:
        temp = content["main"]["temp"]
        temp_max = content["main"]["temp_max"]
        desc = content["weather"][0]["description"]
        
        tts.say(replying.get_reply("weather").format(settings.LOCATION, temp, desc, temp_max))
