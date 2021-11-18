import datetime

from utils import *
import parsing


def format_time(ms):
    h, m = ms_to_hm(ms)
    return f"{pad_maybe(h)}:{pad_maybe(m)} --"


def ms_to_hm(ms):
    return (h := ms // 60), ms - (h * 60)


def message(s):
    return f"---------{s}---------"


def maker(config):
    s = parsing.time_str(config.get('start_time', '00:00'))
    e = parsing.time_str(config.get('end_time', '17:00'))
    r = config.get('resolution', 30)
    start_message = config.get('start_message', '')
    end_message = config.get('end_message', '')
    now = (h := datetime.datetime.now()).hour * 60 + h.minute

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
        if now >= ms and now < (next_ms or (23 * 60 + 59)):
            output.append(t + wrap_ansi(p))
            current_event = True
        elif ms < now:
            output.append(t + wrap_ansi(p, code='strike'))
        else:
            output.append(t + p)
        for x in range(((ms + r) // r) * r, next_ms or e, r):
            # t = format_time(x)
            pad = "         "
            if current_event and now >= x and now < (next_ms or
                                                     (23 * 60 + 59)):
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
