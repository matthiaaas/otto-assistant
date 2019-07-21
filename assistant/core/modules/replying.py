"""
replying
"""

# built-in
import json

# core / core modules
from assistant import settings
from assistant.core.modules import log

"""
get reply
"""
def get_reply(cmd, system=False, module=False, stage=0):
    # keep console clean
    if system == False:
        log.debug("Getting reply...")
    # read replies file
    # and compile json data
    with open(settings.REPLIES_FILE_PATH, "r+", encoding="utf-8") as replies_file:
        replies_file_data = json.load(replies_file)
    # check if call is a system call
    if system == True:
        # get reply in given language and requested stage
        if module == True:
            reply = replies_file_data["system"][cmd[0]][cmd[1]][settings.LANGUAGE]["data"][stage]
        else:
            reply = replies_file_data["system"][cmd][settings.LANGUAGE]["data"][stage]
    else:
        # get reply in given language and requested stage
        reply = replies_file_data[cmd][settings.LANGUAGE]["data"][stage]
    # return matched reply
    return reply
