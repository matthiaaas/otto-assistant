"""
echo
repeats what is
to repeat
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # echo
    AI.say(microphone_input.replace(cmd_text, ""))
