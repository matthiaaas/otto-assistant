# otto-assistant

Otto is a voice assistant originally developed for my Raspberry Pi to control my room from an online UI. He updates his phrases dictionary automatically based on your microphone input.

## Installation

### Requirements

- Python 3.6.7 (recommended for less errors on installation)

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


## Usage

### Getting started

Simply run the `run.py` script by double-clicking or executing from your command prompt.

```
python run.py
```

Now you can use the assistant by saying the default keyword "Otto" followed by your command or question. Wait after the keyword "Otto" for the beep sound.

**Note**: Otto is in English by default. In some cases it might be useful to change the keyword to a word that's typical for your language.

### Examples

Weather
> Otto, what's the weather like?

News
> Otto, what are the news?

Info
> Otto, who is Barack Obama?

To stop the assistant just close the window or - when using the terminal - interrupt the program with the shortcut `ctrl + c`.


## Setup

You can easily change the keyword or city by editing the `settings.py`. Navigate into the `assistant` directory and open the python script in your editor of choice.

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

#### Change API key

default
```py
# openweatherapi key from their site
# (necessary for weather requests)
WEATHER_API_KEY = ""
```

updated: your individual api key (keep it secret)
You can create your own free key [here](https://home.openweathermap.org/api_keys)!
```py
# openweatherapi key from their site
# (necessary for weather requests)
WEATHER_API_KEY = "0abc1def2ghi3jkl4mno5pqr6stu"
```

**Note**: Use lowercase letters.


## Contributing

Feel free to start new pull requests. I appreciate improved code :)
Please take a look at [Gitmoji](https://gitmoji.carloscuesta.me/) for all your commits for consistent messages.

If you wish to have a specific feature supported, start a new issue.

### TODOs

Take a look at the [TODO.md](https://github.com/matthiaaas/otto-assistant/blob/master/TODO.md) for a list of all planned improvements and features - feel free to contribute!

## Troubleshooting

### You get errors?

Take a look at the [TROUBLESHOOTING.md](https://github.com/matthiaaas/otto-assistant/blob/master/TROUBLESHOOTING.md)!
