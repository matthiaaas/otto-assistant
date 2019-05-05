"""
news
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    import time
    
    from packages import news

    AI.say("Suche nach Nachrichten")

    # get 5 ticks from the Google News site
    news = news.News.get(5)

    AI.say("Das sind die Schlagzeilen zur Stunde.")

    for x in range(5):
        AI.say(news[x])
        time.sleep(1)
