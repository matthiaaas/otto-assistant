"""
cpu temperature
reads cpu
temperature
"""
def ex(AI, cmd, cmd_text, microphone_input):
    # imports
    from packages import rpi_manager

    temperature = rpi_manager.RPi.readCPUtemp()

    AI.say("Die CPU hat eine Temperatur von {} Grad Celsius".format(temperature.replace(".", ",")))
