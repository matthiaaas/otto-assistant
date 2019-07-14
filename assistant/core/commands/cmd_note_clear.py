# built-in
import json

# core / core modules
from assistant.core.modules import tts

"""
note clear
remove every note
from list
"""
def ex(cmd):
    notes_file_data = {
        "notes": [
        ]
    }

    # clear file
    with open("data/files/json/notes.json", "w", encoding="utf-8") as notes_file:
        json.dump(notes_file_data, notes_file, indent=2, ensure_ascii=False)

    tts.say("Die Notizliste ist jetzt leer")
