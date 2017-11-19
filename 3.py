# # from collections import OrderedDict
# # from collections import namedtuple
# #
# #
# # class C(object):
# #     pass
# #
# # Card = namedtuple('Card', ['rank', 'suit'])
# #
# #
# # class FrenchDeck:
# #     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# #     suits = 'spades diamonds clubs hearts'.split()
# #
# #     def __init__(self):
# #         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
# #
# #     def __len__(self):
# #         return len(self._cards)
# #
# #     def __getitem__(self, position):
# #         return self._cards[position]
# #
# #
# # beer_card = Card('7', 'diamonds')
# # print(beer_card)
# #
# # deck = FrenchDeck()
# # print(len(deck))
# # print(deck[0], deck[-1])
# #
# # from random import choice
# # print(choice(deck))
# # print(deck[12::13])
# # for card in reversed(deck):
# #     print(card)
# #
# # import time,random
# # print(time.strftime('%H:%M:%S'))
# # a = [(random.randint(1,1000000), random.randint(1,1000000), random.randint(1,1000000),) for x in range(1000000)]
# # print(time.strftime('%H:%M:%S'))
# # a.sort()
# # print(time.strftime('%H:%M:%S'))
#
# # 斐波那契数列
# fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
#
# print(fib(5))
#
#
# # 哈诺塔
# # class Solution(object):
# #     def hanoi_move(self, n, a, b, c):
# #         if n == 1:
# #             print('a' '-->' 'c')
# #         else:
# #             self.hanoi_move(n-1,a, c, b)
# #             print('a' '-->' 'b')
# #             self.hanoi_move(1, a, b, c)
# #             print('a' '-->' 'b')
# #             self.hanoi_move(n-1, b, a, c)
# #             print('a' '-->' 'b')
# #
# # hanoi = Solution()
# # print(hanoi.hanoi_move(3,'a','b','c'))
# def leap_year(year):
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     elif year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# def dayofyear(year, month, day):
#     if leap_year(year):
#         l = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         return sum(l[:month - 1]) + day
#     else:
#         l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         return sum(l[:month - 1]) + day
#
#
# print(dayofyear(2016, 3, 3))
#
# import unittest
#
#
# class TestCase(unittest.TestCase):
#     '''Test for leap year and dayofyear'''
#
#     def test_is_leapyear(self):
#         self.assertTrue(leap_year(2016))
#         self.assertTrue(leap_year(2000))
#         self.assertFalse(leap_year(1900))
#         self.assertFalse(leap_year(2009))
#
#     def test_dayofyear(self):
#         self.assertEqual(63, dayofyear(2016, 3, 3))
#         self.assertEqual(62, dayofyear(2017, 3, 3))
#
#
# if __name__ == '__main__':
#     unittest.main()
#
# def quicksort(arr):
#     less = []
#     pivotlist = []
#     more = []
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         for i in arr:
#             if i < pivot:
#                 less.append(i)
#             elif i > pivot:
#                 more.append(i)
#             else:
#                 pivotlist.append(i)
#
#         less = quicksort(less)
#         more = quicksort(more)
#
#     return less+pivotlist+more
#
#
# def qsort(l):
#     return (qsort([y for y in l[1:] if y < l[0]]) + l[:1] +
#             [y for y in l[1:] if y == l[0] + qsort([y for y in l[1:] if y > l[0]]) if len(l) > 1 else l)

s = 'Hello   World'


# print(s[::-1])
# print(''.join(s[i] for i in range(len(s)-1,-1,-1)))
# print(''.join(s[i] for i in range(len(s)-1 ,-1 ,-1)))
# print(s.split())
# print('  '.join(s.split()[::-1]))
#
# a = [1, 2, 3, 4, 5]
# print([x * 2 for x in a])
# b = []
# for i in range(len(a)):
#     b.append(a[i] * 2)
# print(b)
#
# s1 = {}
# s = [1, 2, 3, 3, 4, 5, 6, 7, 8]
# for i in s:
#     if s.count(i) > 1:
#         s1[i] = s.count(i)
#
# print(s1)

# from collections import Counter
#
# print(Counter(s))
#
# import asyncio
#
#
# async def hello_world():
#     print('Hello World')
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world())
# loop.close()


class Stack():
    def __init__(self):
        self.values = []

    def push(self, o):
        self.values.append(o)

    def pop(self):
        self.values.pop()

    def show(self):
        return self.values


s = Stack()
s.push(1)
s.push(2)

# assert s.pop() == 2
print(s.values)
s.pop()
print(s.values)

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'Hello World'
#
#
# if __name__ == '__main__':
#     app.run()
#
# def simple_coroutine():
#     print('Coroutine started...')
#     x = yield
#     print('Coroutine received:', x)
#
# my_coro = simple_coroutine()
# print(my_coro)
# print(next(my_coro))
# print(my_coro.send(42))

# def averager():
#     total = 0
#     count = 0
#     average = None
#     while True:
#         term = yield average
#         total += term
#         count += 1
#         average = total/count
#
# #预激装饰器
from functools import wraps


# def my_corountine(func):
#     @wraps(func)
#     def primer(*args, **kwargs):
#         gen = func(*args, **kwargs)
#         next(gen)
#         return gen
#     return primer

def wrap(func):
    def call_it(*args, **kwargs):
        'call it'
        print('Before Call:')
        return func(*args, **kwargs)

    return call_it


@wrap
def hello_world():
    print('Hello World')


print(hello_world())

# yield

# def gen():
#     yield from 'AB'
#     yield from range(1,3)
#
# print(list(gen()))
#
# def gen1(*args):
#     for i in args:
#         yield from i
#
# i = 'ABC'
# j = tuple(range(1, 3))
# print(list(gen1(i,j )))

import sys


class AC():
    def __str__(self):
        return 'A'


ac = AC()
print(ac)
sys.stdout.write(str(ac))
