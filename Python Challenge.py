__author__ = 'nickyuan'

# 1. print(2**38)
#    print(pow(2, 38))
# 2. try to solve the offset problem
s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

# s1 = s.split(' ')
# print(s1)
#
# index = 0
# s2 = ''
# for i in s:
#         i = ((ord(i) + 2)-97)%26+97
#         j1 = chr(i)
#         s2 = s2 + j1
# print(s2)

import string

intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
translate = s.maketrans(intab, outtab)

s1 = s.maketrans(translate)
print(s1)


# 3 singleton

class Singelton(object):
    def __init__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singelton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singelton):
    a = 1


class Brog(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Brog, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class MyBrog(Brog):
    a = 1


def singeltonn(cls, *args, **kwargs):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singeltonn()
class MyClass():
    pass
