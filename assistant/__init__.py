"""
assistant
"""

# built-in
import os
import traceback

# core / core modules
from assistant import settings
from assistant.core.modules import log, stt, tts, matching, replying, tasks

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
        print("Basic usage:")
        print(replying.get_reply("greet", system=True).format(settings.KEYWORD))
        print(replying.get_reply("greet", system=True, stage=1).format(settings.KEYWORD))
        print(replying.get_reply("greet", system=True, stage=2).format(settings.KEYWORD))

        tts.say(replying.get_reply("greet", system=True, stage=3))

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
            if self.stop:
                break
            try:
                # listen for keyword
                # wake up on recognized keyword
                if stt.listen_for_keyword():
                    log.debug("Back in loop...")
                    # listen for text input
                    audio = stt.listen()
                    # try resolving input
                    audio_input = stt.recognize(audio)
                    # check if text input received
                    if not audio_input:
                        log.info("Couldn't resolve audio...")
                        continue
                    else:
                        log.info("Catched input '{}'...".format(audio_input))
                    # find match
                    cmd = matching.get_match(audio_input)
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
