"""
set clock
set a timer
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    import time
    
    try:
        defined_input = microphone_input.replace(AI.settings.key_word+" ", "")
        defined_input = defined_input.replace(cmd_text+" ", "")

        # check if a timer is set
        if AI.settings.timer != None:
            AI.say("Du hast einen Timer gesetzt. Dieser wird jetzt gelöscht.")

        defined_input = defined_input.replace(" uhr", "")
        defined_input = defined_input.replace(" sekunden", "")

        new_timer = time.time() + int(defined_input)

        AI.settings.timer = new_timer

        AI.say("Timer auf {} Sekunden gesetzt.".format(defined_input))

    except:
        AI.say("Etwas ist beim setzen des Timers schiefgelaufen. Bitte probiere es nocheinmal.")
