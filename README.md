Main
----

usage: zabbix_hipchat [-h] [--host HOST] [--message_format MESSAGE_FORMAT]
                      token room_id message

positional arguments:
  token
  room_id
  message

optional arguments:
  -h, --help            show this help message and exit
  --host HOST
  --message_format MESSAGE_FORMAT

Example
-------
zabbix_hipchat FDsDs3SiZVGUpsadczcSmrpyV7gdasdR 104523 '<a href="{TRIGGER.URL}">{TRIGGER.STATUS} - {TRIGGER.NAME}</a>' --message_format html
