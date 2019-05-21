"""
speech-to-text
"""

# built-in
import os
import threading
import traceback

# external
import speech_recognition as sr

# core / core modules
from core import settings
from core.modules import log, tts


def setup():
    # recognizer
    global recognizer
    recognizer = sr.Recognizer()
    # improved dynamic and threshold
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 300

"""
listen
> returns audio from microphone
when finished
"""
def listen():
    global audio
    # use microphone as raw input
    with sr.Microphone() as raw_microphone_input:
        log.debug("Listening to ambient...")
        # listen to raw microphone input
        audio = recognizer.listen(raw_microphone_input)
        return audio

"""
recognize
> returns text output from
audio input
"""
def recognize(audio):
    output = None
    # recognize microphone input using selected speech engine
    log.debug("Recognizing audio...")
    # check speech engine
    if settings.STT_ENGINE == "google":
        # try recognizing audio from google
        try:
            # settings query
            output = recognizer.recognize_google(audio, language=settings.LANGUAGE)
            # return output as text
        except sr.UnknownValueError:
            log.debug("Speech engine couldn't resolve audio")
        except sr.RequestError:
            log.error("You need a WiFi connection for Google STT")
        except:
            traceback.print_exc()
            log.error("Unkown exception")
        finally:
            return output

"""
recognize for keyword
(!) CALLBACK of listen_for_keyword
> stops listening if keyword detected
"""
def recognize_for_keyword():
    global keyword_detected
    global new_process
    audio = listen()
    # start new process
    new_process = True
    log.debug("Recognizing keyword...")
    try:
        # recognize input
        input = recognizer.recognize_google(audio, language=settings.LANGUAGE)
        # check if keyword in input
        if settings.KEYWORD in input.lower():
            log.debug("Keyword detected")
            # to stop listening
            keyword_detected = True
        else:
            log.debug("Keyword not detected in '{}'".format(input))
    except sr.UnknownValueError:
        log.debug("Speech engine couldn't resolve audio")
    except sr.RequestError:
        log.error("You need a WiFi connection for Google STT")
    except:
        log.error("Unkown exception")
        traceback.print_exc()

"""
listen for keyword
> returns True if recognized
"""
def listen_for_keyword():
    log.debug("Keyword loop...")
    # global processes
    global keyword_detected
    global new_process
    keyword_detected = False
    new_process = True
    log.info("Waiting for '{}'...".format(settings.KEYWORD))
    while True:
        # quit when keyword is detected
        if keyword_detected:
            break
        # if new process is requested
        if new_process:
            new_process = False
            # start async keyword recognizing thread (start new process)
            threading.Thread(target=recognize_for_keyword).start()
    # play activation sound
    tts.play_mp3(settings.ACTIVATION_SOUND_PATH)
    return True

"""
listen for yes or no
> returns True or False
for yes or no
"""
def listen_for_yn():
    log.info("Waiting for 'ja' or 'nein'")
    while True:
        audio = listen()
        input = recognize(audio)
        if input:
            if "ja" in input.lower():
                log.debug("'Ja' detected")
                return True
            elif "nein" in input.lower():
                log.debug("'Nein' detected")
                return False
            else:
                log.debug("Not detected in '{}'".format(input))
