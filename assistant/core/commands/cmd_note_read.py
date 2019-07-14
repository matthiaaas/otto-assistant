# built-in
import json
import time

# core / core modules
from assistant import settings
from assistant.core.modules import tts

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

    tts.say("Folgendes habe ich für dich notiert")

    if len(notes_file_data["notes"]) == 0:
        tts.say("Du hast noch kein Notizen")

    else:
        # read every note
        for note in notes_file_data["notes"]:
            tts.say(note)
            time.sleep(0.5)
