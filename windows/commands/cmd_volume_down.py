"""
volume DOWN
lighter
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    from packages import volume_manager

    # less sound
    if int(volume_manager.Volume.read().replace("%", "")) > 10:
        volume_manager.Volume.up()
        AI.say("Lautstärke liegt jetzt bei " + volume_manager.Volume.read())

    else:
        AI.say("Lautstärke ist schon auf minimum")
