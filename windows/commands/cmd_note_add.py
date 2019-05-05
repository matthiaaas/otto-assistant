"""
note add
add a new note
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    import json

    # save the command
    # read the file
    with open("data/cache/notes.json", "r+", encoding="utf-8") as notesFile:
        notesFileData = json.load(notesFile)

    # get the new note
    new_note = microphone_input.replace(AI.settings.key_word+" ", "")
    new_note = new_note.replace(cmd_text+" ", "")

    # add note to notes
    notesFileData["notes"].append(new_note)

    # write the list to the file
    with open("data/cache/notes.json", "w", encoding="utf-8") as notesFile:
        json.dump(notesFileData, notesFile, indent=2, ensure_ascii=False)

    AI.say("Ich habe mir {} für dich gemerkt".format(new_note))
