# otto assistant

## Installation

Required external packages

1. gTTS
2. SpeechRecognition
3. playsound
4. PyAudio

Use pip to install all packages
```
pip install <package>
```

## How to use

Just start the `otto.py` file from the command line.
```
python otto.py
```
After that you can use the assistant by saying the keyword "Otto" and your question.

Note: Otto is in German by default

Example:

> Otto, wie ist das Wetter?

or

> Otto, Timer auf 10 Sekunden

## Change keyword

You can easily change the keyword by editing the `settings.json`.
Just change directory to `data/settings` and open the JSON file.
```
cd data/settings
```
```
nano settings.json
```
Then change this line `"keyword": "otto",` to `"keyword": "your_key_word"`.
The assistant will now answer to your new keyword.
