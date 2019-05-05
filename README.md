# otto assistant

Otto is a voice assistant originally developed for my Raspberry Pi to control my room from an online UI.

## Requirements

- Python 3.6.7

## Downloading

If you have [Git](https://git-scm.com/) installed, you can run the following from your terminal:

```
git clone https://github.com/matthiaaas/otto-assistant.git
```

This will clone this repository and download it to your computer.

## Installing packages

Use pip to install all required packages.
Navigate into your OS folder and install all modules from the `requirements.txt`.

```
pip install -r requirements.txt
```

## Usage

Run the `otto.py` script from your command prompt or just start the file by double-clicking.

```
python otto.py
```

After that you can use the assistant by saying the default keyword "Otto" followed by your question.

Note: Otto is in German by default

**Example**

Weather
> Otto, wie ist das Wetter heute?

News
> Otto, was gibt's Neues?

Info
> Otto, wer ist Barack Obama?

To stop the assistant just close the window or - when using the terminal - interrupt the program with `ctrl + c`.

## Setup

You can easily change the keyword or city by editing the `settings.json`.
Just change the directory to `data/settings` and open the JSON file.

**Example**

default
```json
{
  "keyword": "otto",
  "language": "de-DE",
  "location": "berlin"
}
```

changed keyword to "Anna" and location to "Hamburg"
```json
{
  "keyword": "anna",
  "language": "de-DE",
  "location": "hamburg"
}
```

## Contributing

## Troubleshooting
