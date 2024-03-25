def iter_even():
    n = 0
    while True:
        yield n
        n += 2

def iter_odd():
    n = 1
    while True:
        yield n
        n += 2

def iter_power(k):
    n = 1
    while True:
        yield n
        n *= k   