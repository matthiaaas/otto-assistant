"""
assistant
"""

# built-in
import os
import traceback

# core / core modules
from core import settings
from core.modules import log, stt, tts, matching, tasks


instance = None

def main():
    # global access
    global instance
    # instance
    instance = Assistant()


"""
Assistant
"""
class Assistant:
    def __init__(self):
        """
        This is the core of the assistant
        and home of all processes.
        """
        # setup assistant
        self.setup()

        # quit is false
        self.stop = False

    """
    setup
    """
    def setup(self):
        log.debug("Setup...")
        # setup speech-to-text
        stt.setup()
        # setup text-to-speech
        tts.setup()

    """
    clean
    """
    def clean(self):
        log.debug("Cleaning...")

    """
    greet
    """
    def greet(self):
        log.debug("Greeting...")

        print("")
        print(r"         __       __              ")
        print(r"        /\ \__   /\ \__           ")
        print(r"  ___   \ \ ,_\  \ \ ,_\    ___   ")
        print(r" / __`\  \ \ \/   \ \ \/   / __`\ ")
        print(r"/\ \ \ \  \ \ \_   \ \ \_ /\ \ \ \ ")
        print(r"\ \____/   \ \__\   \ \__\\ \____/")
        print(r" \/___/     \/__/    \/__/ \/___/ ")
        print("")
        print("Basic usage:\n")
        print(" Otto *sound*, wie spät ist es?\n")
        print(" Otto *sound*, wie ist das Wetter?")

        tts.say("Hallo, wie kann ich behilflich sein?")

    """
    quit
    """
    def quit(self):
        log.debug("Quitting...")
        # set quit to True
        self.stop = True

        self.clean()

        log.info("Bye!")

    """
    run
    """
    def run(self):
        # greeting
        self.greet()

        # global loop
        while True:
            # check if quit
            if self.stop == True:
                break
            try:
                # listen for keyword
                # wake up on recognized keyword
                if stt.listen_for_keyword():
                    log.debug("Back in loop...")
                    # listen for text input
                    audio = stt.listen()
                    # try resolving input
                    input = stt.recognize(audio)
                    # check if text input received
                    if not input:
                        log.info("Couldn't resolve audio...")
                        continue
                    else:
                        log.info("Catched input '{}'...".format(input))
                    # find match
                    cmd = matching.get_match(input)
                    # execute match
                    matching.execute_match(cmd)
            # user interrupted program
            except KeyboardInterrupt:
                log.info("Detected keyboard interruption...")
                self.quit()
                break
            except:
                log.error("Unexpected error")
                traceback.print_exc()
                break
