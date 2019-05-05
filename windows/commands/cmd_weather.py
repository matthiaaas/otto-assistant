"""
weather
says the todays'
weather
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    from packages import weather

    # check the weather for the set location
    weather_text = weather.Weather.lookup(AI.settings.location)

    AI.say(weather_text)
