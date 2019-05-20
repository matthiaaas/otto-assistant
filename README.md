# otto-assistant

Otto is a voice assistant originally developed for my Raspberry Pi to control my room from an online UI. He upgrades his phrases dictionary automatically based on your microphone input.

## Installation

### Requirements

- Python 3.6.7 (recommended)

### Downloading

If you have [Git](https://git-scm.com/) installed, you can run the following from your terminal:

```
git clone https://github.com/matthiaaas/otto-assistant.git
```

That will clone this repository and download it to your computer.

You can download the [zip file](https://github.com/matthiaaas/otto-assistant/archive/master.zip) using your browser of course.

### Installing libraries

This script uses some external libraries. Use pip to install all required packages. The easiest way to do this is by running the following from your terminal:

```
pip install -r requirements.txt
```

**Note**: This will install the Windows-only package "pypiwin32" on your Linux computer too. Delete this line in the file or install every package manually if you don't want to do so.

### Check installation

To check if everything is operational start the check-installation.py script.

```
python check-installation.py
```

If there's a package missing, this program will help you to fix install.


## Usage

### Getting started

Simply run the `run.py` script by double-clicking or executing from your command prompt.

```
python run.py
```

Now you can use the assistant by saying the default keyword "Otto" followed by your command or question. Wait after the keyword "Otto" for the beep sound.

**Note**: Otto in German by default.

### Examples

Weather
> Otto, wie ist das Wetter heute?

News
> Otto, was gibt's Neues?

Info
> Otto, wer ist Barack Obama?

To stop the assistant just close the windows or - when using the terminal - interrupt the program with the shortcut `ctrl + c`.


## Setup

You can easily change the keyword or city by editing the `settings.py`. Navigate into the `core` directory and open the python script in your editor of choice.

### Examples

#### Change keyword

default
```py
# keyword for waking up
KEYWORD = "otto"
```

updated: keyword is now "Anna"
```py
# keyword for waking up
KEYWORD = "anna"
```

**Note**: Use lowercase letters.

#### Change location

default
```py
# location used for weather requests and more
LOCATION = "berlin"
```

updated: loaction is now "Hamburg"
```py
# location used for weather requests and more
LOCATION = "hamburg"
```

**Note**: Use lowercase letters.


## Contributing

Feel free to start new pull requests. I appreciate improved code :)


## Troubleshooting

### Known bugs

#### "no module named <*>"

Make sure to have the package installed and runned the `check-installation.py` script

If you have multiple Python versions (such as Python 2 and Python 3) installed, make sure to run the script in Python 3

#### "RequestError"

Check your WiFi connection. The assistant cannot resolve audio without a working internet conncetion.

### Not your error?

No problem - just start an issue!
