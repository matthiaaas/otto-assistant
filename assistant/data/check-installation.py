"""
check-installation.py
"""

def check_for_missing_packages():
    print("Checking packages...")
    missing_packages = False
    packages = ["speech_recognition", "pyaudio", "playsound", "gtts"]
    names = ["SpeechRecognition", "PyAudio", "playsound", "gTTS"]
    # check all packages
    for package, name in zip(packages, names):
        print("Checking for package '{}'...".format(package))
        try:
            __import__(package)
            print(" Found...")
        except ModuleNotFoundError:
            missing_packages = True
            print("Failed to load '{0}' package: Use 'pip install {1}' to install".format(package, name))
    return missing_packages

print("Checking installation...")

# check package installation
if not check_for_missing_packages():
    print("> All packages installed")

    print("Now start the run.py in Python 3!")
