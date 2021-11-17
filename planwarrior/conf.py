import configparser


CONFIG_TYPES = {
    'resolution': int,
    'start_time': str,
    'end_time': str,
    'start_message': str,
    'end_message': str,
}

DEFAULT_CONFIG = {
    'resolution': 30,
    'start_time': '8:00',
    'end_time': '17:00',
    'start_message': "Good morning!",
    'end_message': "Have a good evening!",
}


def parse(config):
    c = configparser.ConfigParser()
    c.read(config)
    d = dict(c['planwarrior'])
    for k, v in d.items():
        d[k] = CONFIG_TYPES[k](v)
    return {**DEFAULT_CONFIG, **d}
