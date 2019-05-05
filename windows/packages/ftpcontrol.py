import io
import time
import json
import requests

from ftplib import FTP as ftplib


# open ftp file
with open("data/settings/ftp.json", encoding="utf-8") as ftpFile:
    # load json file content
    ftp_text = json.load(ftpFile)
# declare hostname
ftp_host = ftp_text["host"]
# set username
ftp_username = ftp_text["username"]
ftp_password = ftp_text["password"]


"""
FTP Control
"""
class FTPControl:
    """
    Log read
    """
    def logRead():
        url = "https://otto.matthias.works/ottocontrol/data/log/history.txt"
        # get the data of the log file
        data = requests.get(url).text

        # return
        return data


    """
    Log write
    """
    def logWrite(text):
        # connect to the server
        ftp = ftplib(ftp_host)
        ftp.encoding = "UTF-8"
        # login
        ftp.login(user=ftp_username, passwd=ftp_password)

        data = "{0}<br>\n{1}".format(FTPControl.logRead(), text)

        # encode
        data = io.BytesIO(data.encode("UTF-8"))

        # create file
        ftp.storbinary("STOR data/log/history.txt", data)

        # close connection
        ftp.quit()


    """
    set last request
    """
    def setLastRequest(text):
        # connect to the server
        ftp = ftplib(ftp_host)
        ftp.encoding = "UTF-8"
        # login
        ftp.login(user=ftp_username, passwd=ftp_password)

        timestamp = time.strftime("%H:%M")

        data = '{"time": "' + timestamp + '", "content": "' + text + '"}'

        # encode
        data = io.BytesIO(data.encode("UTF-8"))

        # create file
        ftp.storbinary("STOR data/requests/last_request.json", data)

        # close connection
        ftp.quit()


    """
    set system status
    """
    def setSystemStatus(status):
        # connect to the server
        ftp = ftplib(ftp_host)
        ftp.encoding = "UTF-8"
        # login
        ftp.login(user=ftp_username, passwd=ftp_password)

        timestamp = time.strftime("%y-%m-%d %H:%M:%S")

        data = '{"status": "' + status + '", "restart": "' + timestamp + '"}'

        # encode
        data = io.BytesIO(data.encode("UTF-8"))

        # create file
        ftp.storbinary("STOR data/system/system.json", data)

        # close connection
        ftp.quit()
