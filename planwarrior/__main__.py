import datetime
from pathlib import Path

import cli
import conf
import formatting
import parsing
import utils


def plan_from_dir(dir):
    now = datetime.datetime.now()
    today_file = f"{now.year}{now.month}{now.day}.plan"
    return dir + today_file


def get_plan_file(p, dir):
    return parsing.plan(
        cli.read_file(Path(p or plan_from_dir(dir)).expanduser()))


def main():
    args = cli.parse_args()
    config = conf.parse(args.config)
    plan = get_plan_file(args.plan, config['data_dir'])
    formatter = formatting.maker(config)
    for p, c, n in utils.peek_and_lookback(sorted(plan)):
        print('\n'.join(formatter(p, c, n, plan[c])))


if __name__ == "__main__":
    main()
