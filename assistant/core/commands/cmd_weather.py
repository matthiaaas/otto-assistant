# core
from assistant import settings
# core modules / packages
from assistant.core.modules import tts
from assistant.core.packages import weather

"""
weather
says the todays'
weather
"""
def ex(cmd):
    # check the weather for the set location
    weather_text = weather.Weather.lookup(settings.LOCATION)

    tts.say(weather_text)
