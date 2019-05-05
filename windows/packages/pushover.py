import requests

user_token = "udiefy1nfvyfb6t1vuskyxc59iq6i3"
app_key = "av3mshgr8a63ao5ghx6mnd1ovi5aye"

"""
Pushover
"""
class Pushover:
    """
    Push
    """
    def push(title, message):
        push_data = {
            "token": app_key,
            "user": user_token,
            "title": title,
            "message": message
        }
        requests.post(url="https://api.pushover.net/1/messages.json", data=push_data)
