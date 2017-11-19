__author__ = 'nickyuan'

#使用协程做离散事件仿真

# from itertools import cycle
import threading
import itertools
import time
import sys

write = sys.stdout.write

from functools import namedtuple

Result = namedtuple('Result', 'count average')
#sub gen
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
        return Result(count, average)

#gen
def grouper(results, key):
    while True:
        results[key] = yield from averager()

#client
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)
    report(results)

def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))

data = {
    'girls;kg':
        [40.9, 38.5, 33.3 ,45.7, 44.5],
    'boys;kg':
        [76.8, 67.9, 80.8, 71.3, 77.7]
}

if "__name__" == "__main__":
    main(data)


# i = iter(expr)
# try:
#     y = next(i)
# except StopIteration as _e:
#     r = _e.value
# else:
#     while 1:
#         s = yield y

