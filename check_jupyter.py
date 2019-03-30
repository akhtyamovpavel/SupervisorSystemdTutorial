from credentials import SLACK_URL

import sys
import requests


def send_slack_notification(color):
    color_dict = {
        'good': 'Jupyter is running',
        'danger': 'Jupyter has stopped'
    }
    requests.post(SLACK_URL, json={
         "attachments": [
             {
                 "color": color,
                 "text": color_dict[color]
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

        data_dict = dict([x.split(':') for x in data.split()])

        if data_dict['processname'] == 'jupyter':
            if headers['eventname'] == 'PROCESS_STATE_RUNNING' and data_dict['from_state'] == 'STARTING':
                send_slack_notification('good')
            if headers['eventname'] == 'PROCESS_STATE_STOPPED' and data_dict['from_state'] == 'STOPPING':
                send_slack_notification('danger')
        write_stderr('data :' + data + '\n')
        write_stdout('RESULT 2\nOK')


if __name__ == '__main__':
    main()
    send_slack_notification()
