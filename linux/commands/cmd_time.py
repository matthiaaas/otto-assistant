"""
time
says the current time
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    from datetime import datetime

    # get the time
    uhrzeit = datetime.now().strftime("%H:%M")

    # make the time ready to read
    h = uhrzeit.split(":")[0]
    m = uhrzeit.split(":")[1]

    AI.say("Es ist {0} Uhr {1}".format(h, m))
