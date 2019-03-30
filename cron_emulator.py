from credentials import SLACK_URL

import sys
import subprocess


def write_stdout(state):
    # only eventlistener protocol messages may be sent to stdout
    sys.stdout.write(state)
    sys.stdout.flush()

def write_stderr(state):
    sys.stderr.write(state)
    sys.stderr.flush()


def main(args):
    while True:
        write_stdout('READY\n')
        line = sys.stdin.readline()

        headers = dict([ x.split(':') for x in line.split() ])

        data = sys.stdin.read(int(headers['len']))

        data_dict = dict([x.split(':') for x in data.split()])
        res = subprocess.call(args, stdout=sys.stderr)
        write_stdout('RESULT 2\nOK')


if __name__ == '__main__':
    main(sys.argv[1:])
    send_slack_notification()
