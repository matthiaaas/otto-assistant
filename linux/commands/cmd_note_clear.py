"""
note clear
remove every note
from list
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    import json

    notesFileData = {
        "notes": [
        ]
    }

    # clear file
    with open("data/cache/notes.json", "w", encoding="utf-8") as notesFile:
        json.dump(notesFileData, notesFile, indent=2, ensure_ascii=False)

    AI.say("Die Notizliste ist jetzt leer")
