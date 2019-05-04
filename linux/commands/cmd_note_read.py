"""
note read
says all saved
notes
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    import json
    import time

    # save the command
    # read the file
    with open("data/cache/notes.json", "r+", encoding="utf-8") as notesFile:
        notesFileData = json.load(notesFile)

    AI.say("Folgendes habe ich für dich notiert")

    if len(notesFileData["notes"]) == 0:
        AI.say("Du hast noch kein Notizen")

    else:
        # read every note
        for note in notesFileData["notes"]:
            AI.say(note)
            time.sleep(1)
