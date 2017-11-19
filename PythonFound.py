# def func():
#     global x
#
#     print ('x is', x)
#     x = 2
#     print ('Changed local x to', x)
#
# x = 50
# func()
# print ('Value of x is', x)
#
#
# def func(a1):
#     global a
#
#     a1 = 3
#     a = [2,3,4]
#
# a =[]
# func(a)
# print(a)

# ---------------------------------------------------------------------------------------

# name = (1,2,3)
# print('There is a %s' % (name,))
# print('There is a ' + format(name))
#
# # class Yield():
# #     @staticmethod
# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i
#
# mygenerator = createGenerator()
# print(mygenerator)
# for i in mygenerator:
#     print(i)


# class Bank():
#     crisis = False
#     def create_atm(self):
#         while not self.crisis:
#             yield '$100'
#
# hsbc = Bank()
# cornor_streect_atm = hsbc.create_atm()
# print(cornor_streect_atm.__next__())
# print([cornor_streect_atm.__next__() for cash in range(5)])

# ---------------------------------------------------------------------------------------

# import itertools
#
# horses = [1, 2, 3, 4]
# races = itertools.permutations(horses)
# print(races)
# print(len(list(races)))
#
# age = 35
# print(age.__class__)
#
# def foo():
#     pass
# print(foo.__class__)
#
# print(age.__class__.__class__)


# ---------------------------------------------------------------------------------------

#
#
# class Foo():
#
#     def upper_attr(self, future_class_parent, future_class_attr):
#
#         uppercase_attr = {}
#
#         # 选取所有不以双下划线开始的属性，并把他们大写
#         for name, val in future_class_attr.items():
#             if not name.startwith('__'):
#                 uppercase_attr[name.upper()] = val
#             else:
#                 uppercase_attr[name] = val
#
#         return type(self, future_class_parent, future_class_attr)
#
#     __metaclass__ = upper_attr
#
#     bar = 'bip'
#
# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))

# ---------------------------------------------------------------------------------------

# def print_everything(*args):
#     for count, thing in enumerate(args):
#         print('{0}. {1}'.format(count, thing))
#
# print(print_everything('apple', 'banana', 'orange'))
#
# def table_things(**kwargs):
#     for name, value in kwargs.items():
#         print('{0} = {1}'.format(name, value))
#
# print(table_things(apple='fruit', cabbage='vegetables'))
#
# for i in enumerate(['a', 'aa', 'bb', 'cc']):
#     print(i)

# ---------------------------------------------------------------------------------------

# class A():
#     value = 1
#
#     def add(x, y):
#         return x + y
#
# a = A()
# b = A()

# ---------------------------------------------------------------------------------------

#单例模式

'''
    1、使用__new__方法
'''
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1

'''
    2、共享属性
'''
#创建实例时把所有实例的__dict__指向同一个字典，这样他们具有相同的属性和方法

class Brog(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Brog, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

class MyClass(Brog):
    a = 1

'''
    3、装饰器版本
'''

def singleton(cls, *args, **kwargs):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance()

@singleton
class Myclass:
    pass


'''
    4、import方法
    作为python的模块是天然的单例模式
'''

#mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

#to use
#from mysingleton.py import my_singleton

my_singleton.foo()
# ---------------------------------------------------------------------------------------

# x = 11
#
# class C(object):
#     x = 33
#     def m(self):
#         x = 44
#         self.x = 55
#
# obj = C()
# print(x)
# print(obj.x)
#
# obj.m()
# print(obj.x)
# print(C.x)
#
# print(C.m.x)

# ---------------------------------------------------------------------------------------
# class Base(object):
#     def __init__(self):
#         print('Base Create')
#
# class childA(Base):
#     def __init__(self):
#         print('Create A')
#         Base.__init__(self)
#
# class childB(Base):
#     def __init__(self):
#         print('Create B')
#         super(childB, self).__init__()
#
# base = Base()
# a = childA()
# b = childB()

# print(base)
# print(a)
# print(b)


# ---------------------------------------------------------------------------------------

# class Number(object):
#     def __init__(self, start):
#         self.data = start
#     def __sub__(self, other):
#         return Number(self.data - other)
#
# X = Number(5)
# Y = X - 2
# print(Y.data)
#
# class Indexer(object):
#     # def __init__(self, data):
#     #     self.data = data
#     def __getitem__(self, index):
#         return index ** 2
#
# a = Indexer()
# print(a[2])
# print(a)
#
# for i in range(5):
#     print(a[i], end = ' ')

# import copy
#
# a = (1, 2, 3, 4, 5)
# b = copy.deepcopy(a)
# print(b)
# print(b is a)
#
# a = (1, 2, 3, 4, 5, [])
# b = copy.deepcopy(a)
# print(b)
# print(b is a)
#
# def printa():
#     print("Hello,", end='')
#     print("World")
#     print("Hahaha")
#
# printa()
#
# # import time
# # import timeit
# # def test_while():
# #     i = 0
# #     while i < 20000:
# #         i += 1
# #     return
# # print(timeit.timeit(test_while(), number=10000))
#
# print(range(3))
# print(type(range(3)))
# print(list(range(3)))


# ---------------------------------------------------------------------------------------

# a = [1, 2, 3, 4, 5]
# b = a[2:]
# print(b == a)
# print(b is not a)
# print(a)

from uuid import uuid4

seed = str(uuid4())
a = uuid4()
print(a)

#求两棵树是否相同
# def is_same_tree(p,q):
#     if p == None and q == None:
#         return True
#     elif p and q:
#         return p.val = q.val and is_same_tree(p.left,q.left) and is_same_tree(p.right, q,right)
#     else:
#         return False