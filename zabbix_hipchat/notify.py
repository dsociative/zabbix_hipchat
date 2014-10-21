# -*- coding: utf8 -*-

import argparse
import json

from sh import curl

from zabbix_hipchat.formatter import color


URL = 'https://{host}/v2/room/{room_id}/notification?auth_token={token}'


parser = argparse.ArgumentParser()
parser.add_argument('token')
parser.add_argument('room_id')
parser.add_argument('message')
parser.add_argument('--host', dest='host', default='api.hipchat.com')
parser.add_argument('--message_format', dest='message_format', default='text')
parser.add_argument('--trigger_status', default='PROBLEM')
parser.add_argument('--trigger_severity', type=int, default=2)


def send(host, room_id, token, message, message_format, trigger_status,
         trigger_severity, notify=True):

    print(curl(
        URL.format(host=host, room_id=room_id, token=token),
        d=json.dumps({
            'message': message,
            'message_format': message_format,
            'notify': notify,
            'color': color(trigger_status, trigger_severity)
        }),
        H='Content-type: application/json'
    ))


def main():
    args = parser.parse_args()
    send(
        args.host,
        args.room_id,
        args.token,
        args.message,
        args.message_format,
        args.trigger_status,
        args.trigger_severity
    )


if __name__ == '__main__':
    main()
