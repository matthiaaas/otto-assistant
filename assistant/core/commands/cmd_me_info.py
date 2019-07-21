# core / core modules
from assistant import settings
from assistant.core.modules import tts

"""
me info
some info
about the assistant
"""
def ex(cmd):
    tts.say("Grüzi Servus, ich bin {}. Ich kann dir beim Wetter, bei den Nachrichten und vielem mehr behilflich sein.".format(settings.KEYWORD))
