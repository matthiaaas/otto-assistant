#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

"""
AI
© Matthias, 2019
"""

"""
packages
"""

# built-in functions or packages
import os
import json
import time
import platform

from threading import Thread
from tempfile import NamedTemporaryFile

# self developed packages

# external packages
import speech_recognition as sr
import win32com.client as engine
import playsound


"""
commands
"""

# command packages
from commands import (
    cmd_time,
    cmd_date,
    cmd_weather,
    cmd_weather_forecast,
    cmd_news,
    cmd_echo,
    cmd_note_read,
    cmd_note_add,
    cmd_note_clear,
    cmd_clock_set,
    cmd_clock_reset,
    cmd_google
)

# command packages linked to their keyword
commands = {
    "time": cmd_time,
    "date": cmd_date,
    "weather": cmd_weather,
    "weatherforecast": cmd_weather_forecast,
    "news": cmd_news,
    "echo": cmd_echo,
    "note": cmd_note_read,
    "note_add": cmd_note_add,
    "note_clear": cmd_note_clear,
    "clock_set": cmd_clock_set,
    "clock_reset": cmd_clock_reset,
}


# declare the recognizer instance
recognizer = sr.Recognizer()

# declare tts engine
tts = engine.Dispatch("SAPI.SpVoice")

print("Starting AI...")


"""
AI (class)
"""
class AI:
    """
    Settings and preloaded configurations
    """
    class settings:
        # load the settings file from the settings folder
        with open("data/settings/settings.json") as settingsFile:
            print("Loading settings.json...")
            settings = json.load(settingsFile)

        # define standard variables / settings (from settings.json)
        # set location
        location = settings["location"].lower()
        # declare language
        language = settings["language"]
        # set keyword
        key_word = settings["keyword"].lower()

        # timer
        timer = None

        # close ?
        close = False


    """
    general functions
    """

    """
    check operating system
    > true, if supported
    """
    def checkWorkingSystem():
        # os is windows
        if platform.system() == "Windows" or platform.system() == "Linux":
            return True
        # os is not Windows / Linux
        else:
            # os is not supported
            return False


    """
    log (to console)
    """
    def log(text):
        # log
        print("AI: {}".format(text))


    """
    play .wav file
    from a given directory
    """
    def playWavFile(file):
        # check if file is a .wav file
        if str(file).endswith(".wav"):
            # play the sound file
            playsound.playsound(file, True)
        # file is not a .wav file
        else:
            raise AssertionError


    """
    say
    an input text
    using Google's TTS
    """
    def say(text):
        tts.Speak(text)


    def timerExpired():
        time_set = AI.settings.timer
        # actual time
        time_now = time.time()
        # check if timer is set
        if time_set != None:
            # check if timer expired
            if time_now >= time_set:
                return True
            # else: timer didn't expired
            else:
                return False


    """
    general routine
    """
    def routineLoopGeneral():
        # global loop
        while AI.settings.close != True:
            # check if timer expired
            if AI.timerExpired():
                # play wav file
                AI.playWavFile("files/sound_timeralert.wav")


    """
    control routine
    for online UI support
    (only on RPi version)
    """
    def routineLoopControl():
        # this is a ghost line
        # (originally loop for online UI)
        pass


    """
    setup
    """
    def setup():
        AI.log("AI Setup...")
        # recognizer threshold
        recognizer.dynamic_energy_threshold = False
        recognizer.energy_threshold = 200

        AI.log("Cleaning AI...")
        # this is a ghost line

        AI.log("Starting routines...")
        # start a new thread
        Thread(target=AI.routineLoopGeneral).start()


    """
    clean
    the AI
    """
    def clean():
        AI.log("Cleaning AI...")
        # this is a ghost line

        # close the AI session
        AI.settings.close = True


    """
    speech processing functions
    """

    """
    recognize audio
    record and recognize audio
    using Google's services for
    speech to text
    """
    def recognizeAudio():
        # do this while not recognizing any text
        while True:
            # use microphone as raw input
            with sr.Microphone() as raw_microphone_input:
                AI.log("listening...")
                # listen to raw microphone input
                audio = recognizer.listen(raw_microphone_input)
                # try to recognize text from audio
                try:
                    # recognize microphone input using google
                    AI.log("recognizing...")
                    output = recognizer.recognize_google(audio, language=AI.settings.language)
                    # return the output as text
                    return output
                    break
                # unable to recognize audio
                except:
                    # continue listening
                    continue


    """
    recognize keyword
    check if the key word is in
    an text input (from microphone)
    > true, if input contains key word
    """
    def recognizeKeyword(microphone_input):
        # load key word
        key_word = AI.settings.key_word
        try:
            # check if key word in input
            if key_word in microphone_input:
                # true
                return True
            # bug fixer / keyword otto is not recognized correctly
            # only check for these if the keyword is otto
            elif key_word == "otto":
                if "ortho" in microphone_input.lower():
                    # true
                    return True
                elif "auto" in microphone_input.lower():
                    # true
                    return True
                elif "o2" in microphone_input.lower():
                    # true
                    return True
            else:
                # false
                return False
        except:
            # false
            return False


    """
    find output
    for the given arguments /
    the microphone input
    """
    def findOutput(microphone_input):
        AI.log("thinking...")
        # open phrases file
        with open("data/cache/phrases.json", encoding="utf-8") as phrasesFile:
            phrasesFileData = json.load(phrasesFile)
        # set the cmd to None (no command defined)
        cmd = None
        # set the cmd phrase to None (no phrase defined)
        # for command addition
        cmd_text = None
        # scan the phrases file
        # for every command name
        for cmd_title in phrasesFileData:
            # for every command phrase and keyword
            for cmd_phrase in phrasesFileData[cmd_title][AI.settings.language]["data"]:
                # check if phrase in microphone input
                if cmd_phrase in microphone_input:
                    # phrase is in microphone input
                    # user wants to execute this command
                    cmd = cmd_title
                    cmd_text = cmd_phrase
                    # check if command list contains cmd_title
                    if commands.__contains__(cmd_title):
                        # get the function an execute command
                        commands.get(cmd_title).ex(AI, cmd, cmd_text, microphone_input)
                    # else: the command is not added yet
                    else:
                        # something crazy happened
                        AI.log("rip something crazy happened")
                        AI.say("Etwas komisches ist passiert")
                    break

        # check if cmd is not set yet
        if cmd == None:
            # nothing replied
            # scan the phrases file again
            # for every command name
            for cmd_title in phrasesFileData:
                # check if microphone input contains cmd name
                if phrasesFileData[cmd_title][AI.settings.language]["keyword"] in microphone_input:
                    # ask if the user wants to execute the command
                    AI.say("Möchtest du den Befehl {} ausführen?".format(phrasesFileData[cmd_title][AI.settings.language]["keyword"]))
                    y_n_microphone_input = None
                    # listen to ambient (for yes or no)
                    y_n_microphone_input = AI.recognizeAudio().lower()
                    AI.log(y_n_microphone_input)
                    # check if input contains 'ja'
                    if "ja" in y_n_microphone_input:
                        # read the phrases file
                        with open("data/cache/phrases.json", "r+", encoding="utf-8") as phrasesFile:
                            phrasesFileData = json.load(phrasesFile)
                        # add the new phrase to the command list
                        phrasesFileData[cmd_title][AI.settings.language]["data"].append(microphone_input)
                        # write the list to the file
                        with open("data/cache/phrases.json", "r+", encoding="utf-8") as phrasesFile:
                            json.dump(phrasesFileData, phrasesFile, indent=2, ensure_ascii=False)
                        AI.say("Ich habe den Befehl hinzugefügt")
                        # set the cmd and reply
                        cmd = cmd_title
                        AI.findOutput(microphone_input)
                        break
                    # input doesn't contain 'ja'
                    # check if input contains 'nein'
                    elif "nein" in microphone_input:
                        cmd = "EXIT"

        # google
        if cmd == None:
            # try to find a result using google search
             try:
                 AI.log("Google Search...")
                 # try to get a result from google search
                 cmd_google.ex(AI, "google", "google", microphone_input)
                 cmd = "google"

             except Exception as e:
                 AI.log("Google Search Error...")

        # nothing can help you
        if cmd == None:
            AI.say("Ich konnte sie leider nicht verstehen")
            # save the command
            # read the not used file including phrases
            with open("data/log/bin.json", "r+", encoding="utf-8") as nuFile:
                nuFileData = json.load(nuFile)
            # add the phrase to the list
            nuFileData["unknown"].append(microphone_input)
            # write the new phrase to the file
            with open("data/log/bin.json", "r+", encoding="utf-8") as nuFile:
                json.dump(nuFileData, nuFile, indent=2, ensure_ascii=False)