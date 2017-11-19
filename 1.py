# item = [{}] * 10
# item[0]['key']='value'
# print(item)
#
#
# import requests
# from flask import Flask, request
#
# a = requests.get()
# b = request.args.get()

# import socket
#
# host = ''
# port = 51423
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind((host, port))
# s.listen(1)
#
# print("Server is running on port %d; Press Ctrl-C to terminate" % port)
#
# while 1:
#     clientsock, clientaddr = s.accept()
#     clientfile = clientsock.makefile('rw', 0)
#     clientfile.write("Welcome, " + str(clientaddr) + "\n")
#     clientfile.write("Please enter a string: ")
#     line = clientfile.read().split()
#     clientfile.write("You entered %d characters.\n" % len(line))
#     clientfile.close()
#     clientsock.close()

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

print(A0)


def print_directory_contents(sPath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


'''---------------------------------------------------------------------------------------------------------------'''

# def f(x, l=[]):
#     for i in range(x):
#         l.append(i * i)
#     print(l)
#
# f(2)
# f(3, [3, 2, 1])
# f(3)
# f(4)


            # 补充代码


#
# import cProfile
# import random
#
# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     return [i*i for i in l2]
#
# def f2(lIn):
#     l1 = [i for i in lIn if i<0.5]
#     l2 = sorted(l1)
#     return [i*i for i in l2]
#
# def f3(lIn):
#     l1 = [i*i for i in lIn]
#     l2 = sorted(l1)
#     return [i for i in l1 if i<(0.5*0.5)]
#
# lIn = [random.random() for i in range(100000)]
# cProfile.run('f1(lIn)')
# cProfile.run('f2(lIn)')
# cProfile.run('f3(lIn)')


'''---------------------------------------------------------------------------------------------------------------'''
#
# from gevent import monkey; monkey.patch_socket()
# import gevent
#
#
# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#
# gevent1 = gevent.spawn(f, 5)
# gevent2 = gevent.spawn(f, 5)
# gevent3 = gevent.spawn(f, 5)
#
# gevent1.join()
# gevent2.join()
# gevent3.join()

'''---------------------------------------------------------------------------------------------------------------'''

# import sys
# print("My Python version is : {}".format(sys.version))
#
# print('{},{}'.format('aaa',18))
# print('{0},{1},{2}'.format('aaa',18,333))
# print('{name},{age}'.format(age=18, name='aaa'))
# print("{:,}".format(1234567899999))
# print('{:>9}'.format(189))

'''---------------------------------------------------------------------------------------------------------------'''

