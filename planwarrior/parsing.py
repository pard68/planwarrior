def time_str(s):
    h, m = [int(x) for x in s.split(':')]
    return h * 60 + m


def plan(plan):
    return {
        time_str((y := x.strip().split(' '))[0]): ' '.join(y[1:])
        for x in plan.strip().splitlines()
    }
