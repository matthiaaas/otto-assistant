"""
text-to-speech
"""

# built-in
import platform

from tempfile import NamedTemporaryFile as named_temp_file

# external
from playsound import playsound

# core / core modules
from assistant import settings
from assistant.core.modules import log


engine = None

def setup():
    global engine
    # tts engine setup
    # detect OS
    if platform.system() == "Windows" and settings.TTS_AUTODETECT:
        try:
            # import module
            import win32com.client as win32com
            engine = win32com.Dispatch("SAPI.SpVoice")
        except ModuleNotFoundError:
            log.error("Couldn't find a module named 'win32com.client'")
            log.error("Check installation or install via 'pip install pypiwin32'")
    else:
        try:
            # import module
            from gtts import gTTS
            engine = gTTS
        except ModuleNotFoundError:
            log.error("Couldn't find a module named 'gtts'")
            log.error("Check installation or install via 'pip install gtts'")
        log.info("(!) Using slow TTS engine on your OS")

"""
play mp3
"""
def play_mp3(file):
    if file.endswith(".mp3"):
        playsound(file, True)
    else:
        log.error("Is not a mp3 file")

"""
say
"""
def say(text):
    if settings.TTS_SUBTITLE:
        log.info(text)
    # Windows
    if platform.system() == "Windows" and settings.TTS_AUTODETECT:
        engine.Speak(text)
    # other OS
    else:
        with named_temp_file() as f:
            # google server request
            output = engine(text=text, lang=settings.LANGUAGE_SHORT)
            # save received file
            output.save(f.name+".mp3")
            # play
            play_mp3(f.name+".mp3")
