import argparse


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def parse_args():
    default_config_path = "$HOME/.config/planwarrior/config.ini"
    p = argparse.ArgumentParser(description='Terminal dayplan visualizer')
    p.add_argument('--config', metavar='c', default=default_config_path,
                   type=str, help='path to config file')
    p.add_argument('plan', type=str, help='path to day plan file')
    return p.parse_args()
