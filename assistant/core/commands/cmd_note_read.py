# built-in
import json
import time

# core / core modules
from assistant import settings
from assistant.core.modules import tts, replying

"""
note read
says all saved
notes
"""
def ex(cmd):
    # save the command
    # read the file
    with open("data/files/json/notes.json", "r+", encoding="utf-8") as notes_file:
        notes_file_data = json.load(notes_file)

    tts.say(replying.get_reply("note_read"))

    if len(notes_file_data["notes"]) == 0:
        tts.say(replying.get_reply("note_read", stage=1))

    else:
        # read every note
        for note in notes_file_data["notes"]:
            tts.say(note)
            time.sleep(0.5)
