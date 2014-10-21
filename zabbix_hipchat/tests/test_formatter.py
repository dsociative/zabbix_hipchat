from zabbix_hipchat.formatter import color


def test_color():
    assert color('PROBLEM') == 'yellow'
    assert color('OK') == 'green'


def test_color_with_severity():
    assert color('PROBLEM', 2) == 'yellow'
    assert color('PROBLEM', 3) == 'red'
    assert color('PROBLEM', 4) == 'red'
    assert color('PROBLEM', 1) == 'gray'
    assert color('PROBLEM', 0) == 'gray'
    assert color('OK', 3) == 'green'
