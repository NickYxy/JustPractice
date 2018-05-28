__author__ = 'nickyuan'

# class SimpleItemContainer(object):
#     def __init__(self, id, item_container):
#         self.id = id
#         self.data = {}
#         for item in item_container:
#             self.data[item.id] = item
#
# containerA = SimpleItemContainer(2,['a','b','c'])
# print(containerA)

from delorean import Delorean


d = Delorean()
d = d.shift("Asia/Shanghai")


from requests import request

print(d)
print(d.datetime, d.date)

import wget

print(wget.download("http://music.163.com/#/song?id=27678693"))
