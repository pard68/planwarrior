import formatting
import utils
import parsing


def main():
    config = {
        'resolution': 30,
        'start_time': '8:00',
        'end_time': '17:00',
        'start_message': "Good morning!",
        'end_message': "Have a good evening!",
    }
    plan = """
08:00 Plan day
08:30 Design planwarrior
10:00 Work on planwarrior poc
12:00 break for lunch
13:00 Finalize planwarrior poc
16:00 Publish planwarrior to GH
16:55 be lauded for my amazing snek skillz
    """
    parsed_plan = parsing.plan(plan)
    # times = {x: '' for x in range(0, 24*60, config.get('resolution', 30))}
    # merged_plan = {**times, **parsed_plan}
    formatter = formatting.maker(config)
    for p, c, n in utils.peek_and_lookback(sorted(parsed_plan)):
        print('\n'.join(formatter(p, c, n, parsed_plan[c])))


if __name__ == "__main__":
    main()
