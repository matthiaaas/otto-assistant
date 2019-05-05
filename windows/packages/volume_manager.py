"""
Volume
"""

import os


class Volume:
    """
    Read
    """
    def read():
        # the cmd to get only the master volume
        cmd = "amixer get Master | grep 'Right' | awk -F'[][]' '{ print $2 }'"

        # read the current volume
        volume = os.popen(cmd).read()

        # give back
        return volume


    """
    Up
    """
    def up():
        # the cmd to set the new volume
        cmd = "amixer set Master"

        current_volume = int(Volume.read().replace("%", ""))

        # check, if the volume is already 100%
        if current_volume < 100:
            # set new volume (+ 10%)
            new_volume = str(current_volume + 10) + "%"
            # do
            os.popen(cmd + " " + new_volume)
            # out
            # print("Volume is now " + new_volume)

        # volume is 100%
        else:
            # print("Volume is already 100%")
            pass


    """
    Down
    """
    def down():
        # the cmd to set the new volume
        cmd = "amixer set Master"

        current_volume = int(Volume.read().replace("%", ""))

        # check, if the volume is already 100%
        if current_volume > 0:
            # set new volume (+ 10%)
            new_volume = str(current_volume - 10) + "%"
            # do
            os.popen(cmd + " " + new_volume)
            # out
            # print("Volume is now " + new_volume)

        # volume is 0%
        else:
            # print("Volume is already 0%")
            pass
