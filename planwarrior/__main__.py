import cli
import conf
import formatting
import parsing
import utils


def main():
    args = cli.parse_args()
    config = conf.parse(args.config)
    plan = parsing.plan(cli.read_file(args.plan))
    formatter = formatting.maker(config)
    for p, c, n in utils.peek_and_lookback(sorted(plan)):
        print('\n'.join(formatter(p, c, n, plan[c])))


if __name__ == "__main__":
    main()
