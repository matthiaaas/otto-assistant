"""
SeTtINgs
"""

# built-in
import logging

# keyword for waking up
KEYWORD = "otto"

# sst/tts language used for recognizing
LANGUAGE = "de-DE"
LANGUAGE_SHORT = "de"

# location used for weather requests and more
LOCATION = "buehl"

# the stt speech engine used to recognize audio
# (at the moment only google available)
STT_ENGINE = "google"

# the tts engine used to reply
# (NOT used at the moment: auto-detect)
TTS_ENGINE = ""
# subtitles
# set to 'false' if you don't want to print every tts output to console
TTS_SUBTITLE = True
# set to false to deactivate auto OS detection for tts engine
# (you will need to use the python library gTTS)
TTS_AUTODETECT = True

# os used for specific raspberry pi software
# (NOT used at the moment: auto-detect)
OPERATING_SYSTEM = ""

# activation sound path on keyword
ACTIVATION_SOUND_PATH = "data/files/sound/activation.mp3"

# phrases file path for matching
PHRASES_FILE_PATH = "data/files/json/phrases.json"

# logger definitions
LOGGER_NAME = "otto"
LOGGER_LEVEL = logging.DEBUG
