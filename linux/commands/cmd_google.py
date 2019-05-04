"""
Google
try to find a result
from Google Search
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    from packages import googlesearch

    search_this = microphone_input.replace("otto ", "")

    # try to get a result from google search
    result = googlesearch.Search.get(search_this)

    AI.say(result)
