# Troubleshooting

## Runtime errors

Errors while executing the assistant

### ImportError: no module named *

Make sure to have the package installed and ran the `check-installation.py` script.

If you have multiple Python versions (such as Python 2 and Python 3) installed, make sure to run the script in Python 3

### RequestError

Check your WiFi. The assistant cannot resolve audio without a working internet conncetion.

### ValueError: Namespace Gst is not available

Run `sudo apt-get install python-gst-1.0`.

### OSError: FLAC conversion utility not available

Install FLAC via `sudo apt-get install flac`.

## Installation errors

Errors while installing packages or modules

### failed building wheel for pyaudio

If you're unable to install PyAudio using `pip install pyaudio`, check out [this issue](https://github.com/SlapBot/stephanie-va/issues/8#issuecomment-307617796).

## Other?

No problem! Feel free to start a [new issue](https://github.com/matthiaaas/otto-assistant/issues/new).
