"""
speech-to-text
"""

# built-in
import os
import traceback

# external
import speech_recognition as sr

from pocketsphinx import LiveSpeech, get_model_path

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
            log.info("Speech engine couldn't resolve audio")
        except sr.RequestError:
            log.info("You need a WiFi connection for Google STT")
        except:
            traceback.print_exc()
            log.info("Unkown exception")
        finally:
            return output

"""
listen for keyword
> returns True if recognized
"""
def listen_for_keyword():
    log.info("Waiting for '{}'".format(settings.KEYWORD))
    while True:
        audio = listen()
        input = recognize(audio)
        if input:
            if settings.KEYWORD in input.lower():
                log.debug("Keyword detected")
                tts.play_mp3(settings.ACTIVATION_SOUND_PATH)
                return True
                break
            else:
                log.debug("Keyword not detected in '{}'".format(input))

    # not implemented because of missing German language model
    # for keyword detection
    """
    # path
    hmm=os.path.join(model_path, "de-de"),
    lm=os.path.join(model_path, "de-de.lm.bin"),
    dic=os.path.join(model_path, "cmudict-de-de.dic")

    model_path = get_model_path()
    # live speech
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        # path
        hmm=os.path.join(model_path, "acoustic-model"),
        lm=os.path.join(model_path, "language-model.lm.bin"),
        dic=os.path.join(model_path, "pronounciation-dictionary.dict")
    )
    # scan every phrase for keyword
    for phrase in speech:
        log.info(phrase)
        # check if keyword in phrase
        if settings.KEYWORD in str(phrase):
            # wake up
            return True
    """

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
                break
            elif "nein" in input.lower():
                log.debug("'Nein' detected")
                return False
                break
            else:
                log.debug("Not detected in '{}'".format(input))
