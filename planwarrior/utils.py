def peek_and_lookback(cur):
    prv = [None] + cur[:-1]
    nxt = cur[1:] + [None]
    return zip(prv, cur, nxt)


def peek(x):
    p = x[1:]
    p.append(None)
    return zip(x, p)


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


def pad_maybe(i):
    return str(i) if len(str(i)) > 1 else f"0{i}"
