# core / core modules
from assistant.core.modules import tts

"""
echo
repeats what is
to repeat
"""
def ex(cmd):
    # echo
    tts.say(cmd["input"].replace(cmd["text"] + " ", ""))
