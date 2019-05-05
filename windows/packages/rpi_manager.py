"""
Raspberry Pi
"""

import os


class RPi:
    """
    read CPU temperature
    """
    def readCPUtemp():
        cmd = "vcgencmd measure_temp"

        # read the actual temperature
        temperature = os.popen(cmd).read()

        temperature = temperature.replace("temp=", "")
        temperature = temperature.replace("'C", "")

        return temperature
