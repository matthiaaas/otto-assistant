"""
set clock
set a timer
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # reset
    AI.settings.timer = None

    AI.say("Timer zurückgesetzt")
