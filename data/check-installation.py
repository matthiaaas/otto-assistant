"""
check-installation.py
"""

def check_package_installation():
    missing_packages = False
    print("Checking packages...")
    # sr
    try:
        import speech_recognition
    except ModuleNotFoundError:
        missing_packages = True
        print("Check installation of the speech recognition module!")
        print("Run 'pip install SpeechRecognition'")
    # pyaudio
    try:
        import pyaudio
    except ModuleNotFoundError:
        missing_packages = True
        print("Check installation of pyaudio!")
        print("Run 'pip install PyAudio'")
    # playsound
    try:
        import playsound
    except ModuleNotFoundError:
        missing_packages = True
        print("Check installation of playsound!")
        print("Run 'pip install playsound'")
    # gtts
    try:
        import gtts
    except ModuleNotFoundError:
        missing_packages = True
        print("Check installation of gTTS!")
        print("Run 'pip install gtts'")

print("Checking installation...")

# check package installation
if not check_package_installation():
    print("> All packages installed")

    print("Now start the run.py in Python 3!")
