def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

def make_upper_case(s):
    for i in s: i ==i.upper()
    return i

def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'