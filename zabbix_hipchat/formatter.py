
COLOR_TABLE = {
    0: 'gray',
    1: 'gray',
    2: 'yellow',
    3: 'red',
    4: 'red',
}


def color(trigger_status, trigger_serverity=2):
    if trigger_status == 'PROBLEM':
        return COLOR_TABLE.get(trigger_serverity, 'yellow')
    else:
        return 'green'
