# built-in
import json

# core / core modules
from assistant import settings
from assistant.core.modules import tts, replying

"""
note add
add a new note
"""
def ex(cmd):
    # save the command
    # read the file
    with open("data/files/json/notes.json", "r+", encoding="utf-8") as notes_file:
        notes_file_data = json.load(notes_file)

    # get the new note
    # new_note = cmd["input"].replace(settings.KEYWORD + " ", "")
    new_note = cmd["input"].replace(cmd["text"] + " ", "")

    # add note to notes
    notes_file_data["notes"].append(new_note)

    # write the list to the file
    with open("data/files/json/notes.json", "w", encoding="utf-8") as notes_file:
        json.dump(notes_file_data, notes_file, indent=2, ensure_ascii=False)

    tts.say(replying.get_reply("note_add").format(new_note))
