"""
volume UP
louder
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    from packages import volume_manager

    # more sound
    if int(volume_manager.Volume.read().replace("%", "")) < 100:
        volume_manager.Volume.up()
        AI.say("Lautstärke liegt jetzt bei " + volume_manager.Volume.read())

    else:
        AI.say("Lautstärke ist schon auf maximum")
