#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

"""
Otto assistant
© Matthias, 2019
"""

print("Starting Otto...")

# import ai package
from ai import AI

"""
This is the main part of
the (AI) assistant.
"""
try:
    # check if the system is supported
    AI.log("Checking OS...")
    if AI.checkWorkingSystem():
        # system is supported
        # set up the AI
        AI.setup()
        # log that AI is ready
        AI.log(" ")
        AI.log("AI is ready")
        AI.log(" ")
        AI.say("Ich bin jetzt bereit!")
        while True:
            # recognize audio from ambient
            # save it as microphone input in lowercase letters
            microphone_input = AI.recognizeAudio().lower()
            # log microphone input
            AI.log(microphone_input)
            # check if keyword is in microphone input
            if AI.recognizeKeyword(microphone_input):
                # check if only 'otto' in microphone input
                if AI.settings.key_word == microphone_input:
                    # expect command after keyword:
                    # user wants to say the command after a short sound
                    AI.playWavFile("files/sound_activation.wav")
                    # recognize audio from ambient
                    # save it as microphone input in lowercase letters
                    microphone_input = AI.recognizeAudio().lower()
                    # log microphone input
                    AI.log(microphone_input)
                    # find output and try to execute command
                    AI.findOutput(microphone_input)
                # find a output for the given arguments
                else:
                    # keyword is in microphone input
                    # find output and try to execute command
                    AI.findOutput(microphone_input)

    # system is not supported
    else:
        AI.log("Unsupported system")
        AI.log("Make sure to run this script on Windows or a Linux distribution")

# user interrupted program
except KeyboardInterrupt:
    # clean up the AI
    # clean Exit
    AI.clean()
    AI.log("AI shutdown successful")

# fatal error
except Exception as e:
    try:
        AI.log(e)
        # tips
        AI.log("You need to be connect to the internet")
        AI.log("Check installation of essential packages from pip")
        # try to clean
        AI.clean()

    # rip
    except:
        pass
