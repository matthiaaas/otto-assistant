"""
matching
"""

# built-in
import os
import json

# core / core modules
from assistant import settings
from assistant.core.modules import log, tts, stt, replying

# core command packages
from assistant.core.commands import (
    cmd_time,
    cmd_date,
    cmd_weather,
    cmd_weather_forecast,
    cmd_news,
    cmd_echo,
    cmd_note_read,
    cmd_note_add,
    cmd_note_clear,
    cmd_me_info,
    cmd_google
)

# command packages linked to their execution keyword
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
    "me_info": cmd_me_info
}


def setup():
    pass

"""
check match
"""
def check_match(input):
    cmd = {"name": None, "text": None, "input": input}
    # get phrases file data as json
    with open(settings.PHRASES_FILE_PATH, encoding="utf-8") as phrases_file:
        phrases_file_data = json.load(phrases_file)
    # scan phrases file for match
    # for every command title
    for cmd_title in phrases_file_data:
        # for every data line of command title (in prefered language)
        for cmd_phrase in phrases_file_data[cmd_title][settings.LANGUAGE]["data"]:
            # check if in input
            if cmd_phrase in input.lower():
                # ready for return
                cmd = {"name": cmd_title, "text": cmd_phrase, "input": input}
                return cmd

"""
test match
"""
def test_match(input):
    cmd = {"name": None, "text": None, "input": input}
    # get phrases file data as json
    with open(settings.PHRASES_FILE_PATH, encoding="utf-8") as phrases_file:
        phrases_file_data = json.load(phrases_file)
    # scan phrases file for match
    # for every command title
    for cmd_title in phrases_file_data:
        keyword = phrases_file_data[cmd_title][settings.LANGUAGE]["keyword"]
        # check if keyword in input
        if keyword in input.lower():
            tts.say(replying.get_reply(["matching", "ask"], system=True, module=True).format(keyword))
            yn_input = stt.listen_for_yn()
            # if 'yes'
            if yn_input:
                # read the phrases file
                with open(settings.PHRASES_FILE_PATH, "r+", encoding="utf-8") as phrases_file:
                    phrases_file_data = json.load(phrases_file)
                # add the new phrase to the command list
                phrases_file_data[cmd_title][settings.LANGUAGE]["data"].append(input.lower())
                # write the list to the file
                with open(settings.PHRASES_FILE_PATH, "r+", encoding="utf-8") as phrases_file:
                    json.dump(phrases_file_data, phrases_file, indent=2, ensure_ascii=False)
                tts.say(replying.get_reply(["matching", "added"], system=True, module=True))
                cmd = {"name": cmd_title, "text": phrases_file_data[cmd_title][settings.LANGUAGE]["data"][0], "input": input}
                return cmd

"""
google match
"""
def google_match(input):
    log.debug("Google Search...")
    try:
        cmd_google.ex(input)
        cmd = {"name": "google", "text": input, "input": input}
        return cmd
    except:
        log.debug("No result from Google Search...")

"""
get match
"""
def get_match(input):
    log.debug("Matching...")

    cmd = {"name": None, "text": None, "input": input}

    # all jobs in correct order
    jobs = [check_match, test_match, google_match]

    # for every job
    for job in range(len(jobs)):
        cmd = jobs[job](input)
        # check if matched
        if cmd != None:
            log.debug("Matched command '{}'".format(cmd["name"]))
            return cmd
        else:
            # next stage matching
            continue
    # unable to match
    log.debug("Couldn't match command from input...")

"""
execute match
"""
def execute_match(cmd):
    log.debug("Executing...")
    #
    try:
        # check if command exists as python script
        if commands.__contains__(cmd["name"]):
            log.debug("Replying...")
            commands.get(cmd["name"]).ex(cmd)
        elif cmd["name"] == "google":
            log.debug("Already executed...")
        else:
            log.error("Couldn't match command script")
    # type error: no command found
    except TypeError:
        tts.say(replying.get_reply(["matching", "fail"], system=True, module=True))
