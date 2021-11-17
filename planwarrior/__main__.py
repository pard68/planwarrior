import datetime
import itertools


def parse_time_str(s):
    h, m = [int(x) for x in s.split(':')]
    return h*60+m


def parse_plan(plan):
    return {parse_time_str((y := x.strip().split(' '))[0]): ' '.join(y[1:])
            for x in plan.strip().splitlines()}


def pad_maybe(i):
    return str(i) if len(str(i)) > 1 else f"0{i}"


def _make_formatter(config):
    s = parse_time_str(config.get('start_time', '00:00'))
    e = parse_time_str(config.get('end_time', '17:00'))
    r = config.get('resolution', 30)
    start_message = config.get('start_message', '')
    end_message = config.get('end_message', '')
    now = (h := datetime.datetime.now()).hour * 60 + h.minute

    def format_time(ms):
        h, m = ms_to_hm(ms)
        return f"{pad_maybe(h)}:{pad_maybe(m)} --"

    def ms_to_hm(ms):
        return (h := ms // 60), ms - (h*60)

    def message(s):
        return f"---------{s}---------"

    def formatter(prev_ms, ms, next_ms, p):
        output = []
        current_event = False
        if not prev_ms and ms > s:
            output.append(message(start_message))
            for x in range(s, ms - 1, r):
                output.append(format_time(x) + " ...")
        elif s == ms:
            output.append(message(start_message))
        if e == ms:
            output.append(message(end_message))
        t = f"{format_time(ms)} "
        if now >= ms and now < next_ms:
            output.append(t + wrap_ansi(p))
            current_event = True
        elif ms < now:
            output.append(t + wrap_ansi(p, code='strike'))
        else:
            output.append(t+p)
        for x in range(((ms + r) // r) * r, next_ms or e, r):
            # t = format_time(x)
            pad = "         "
            if current_event and now >= x and now < next_ms:
                if now < x + r:
                    output.append(
                        wrap_ansi(pad + wrap_ansi("now", code='bold')))
                else:
                    output.append(wrap_ansi(pad + "..."))
            else:
                output.append(pad + "...")
        if not next_ms and ms < e:
            output.append(message(end_message))
        return output
    return formatter


def wrap_ansi(s, code='green'):
    c = {
        'bold': ['\033[1m', '\033[00m'],
        'italic': ['\033[3m', '\033[00m'],
        'underline': ['\033[4m', '\033[00m'],
        'strike': ['\033[9m', '\033[00m'],
        'green': ['\033[0;32m', '\033[00m'],
    }
    d = 'green'
    return f"{c.get(code, d)[0]}{s}{c.get(code, d)[1]}"


def peek_and_lookback(cur):
    prv = [None] + cur[:-1]
    nxt = cur[1:] + [None]
    return zip(prv, cur, nxt)


def peek(x):
    p = x[1:]
    p.append(None)
    return zip(x, p)


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
    parsed_plan = parse_plan(plan)
    # times = {x: '' for x in range(0, 24*60, config.get('resolution', 30))}
    # merged_plan = {**times, **parsed_plan}
    formatter = _make_formatter(config)
    for p, c, n in peek_and_lookback(sorted(parsed_plan)):
        print('\n'.join(formatter(p, c, n, parsed_plan[c])))


if __name__ == "__main__":
    main()
