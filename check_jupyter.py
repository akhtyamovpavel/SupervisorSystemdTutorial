from credentials import SLACK_URL

import sys
import requests


def send_slack_notification():
    requests.post(SLACK_URL, json={
         "attachments": [
             {
                 "color": "good",
                 "text": "Jupyter is running"
             }
        ]}
    )


def write_stdout(state):
    # only eventlistener protocol messages may be sent to stdout
    sys.stdout.write(state)
    sys.stdout.flush()

def write_stderr(state):
    sys.stderr.write(state)
    sys.stderr.flush()


def main():
    while True:
        write_stdout('READY\n')
        line = sys.stdin.readline()
        write_stderr('meta: ' + line + '\n')

        headers = dict([ x.split(':') for x in line.split() ])

        data = sys.stdin.read(int(headers['len']))
        write_stderr('data :' + data + '\n')
        write_stdout('RESULT 2\nOK')


if __name__ == '__main__':
    main()
    send_slack_notification()
