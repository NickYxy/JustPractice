__author__ = 'nickyuan'

# asyncio tutorial
#
# asyncio提供了完善的异步IO支持；
#
# 异步操作需要在coroutine中通过yield from完成；
#
# 多个coroutine可以封装成一组Task然后并发执行。

import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hello World')
#     # 异步调用asyncio.sleep()
#     r = yield from asyncio.sleep(1)
#     print('Hello again!')
#
#
# # 获取Event loop
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# asyncio.coroutine会把一个generator标记为coroutine类型，然后我们就把这个coroutine扔到Eventloop中去执行
# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
# 而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

import threading


# @asyncio.coroutine
# def task():
#     print('Hello World!(%s)' % threading.current_thread())
#     yield from asyncio.sleep(1)
#     print('Hello Again!(%s' % threading.current_thread())
#
#
# @asyncio.coroutine
# def task1():
#     print('Hello Task1!(%s)' % threading.current_thread())
#     yield from asyncio.sleep(1)
#     print('Hello Task1 Again!(%s' % threading.current_thread())
#
#
# loop1 = asyncio.get_event_loop()
# tasks = [task(), task1()]
# loop1.run_until_complete(asyncio.wait(tasks))
# loop1.close()


# 在这个例子中,可以发现一旦协程阻塞,就会中断当前的协程处理,然后切换到下一个消息处理,同时把阻塞的协程加入消息队列的后面.
#
# task1遇到阻塞，中断，调准到tasks里的task执行，然后又遇到阻塞，跳转到task1执行，执行完跳转到task
#
# 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
#
# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。


# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop2 = asyncio.get_event_loop()
task3 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop2.run_until_complete(asyncio.wait(task3))
loop2.close()


# 写一个传统的生产消费者模型
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s...' % n)
        r = '200 ok'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[Producer] Producing %s...' % n)
        r = c.send(n)
        print('[Producer] Consumer return: %s' % r)
    c.close()


c = consumer()
producer(c)


# 注意到consumer函数是一个generator，把一个consumer传入produce后：
#
# 首先调用c.send(None)启动生成器；
#
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
# produce拿到consumer处理的结果，继续生产下一条消息；
#
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
#
# 最后套用Donald Knuth的一句话总结协程的特点：
#
# “子程序就是协程的一种特例。”

def consumer():
    r = ''

    print('*' * 10, '1', '*' * 10)
    while True:
        print('*' * 10, '2', '*' * 10)
        n = yield r
        # if not n:
        #     print('*' * 10, '3', '*' * 10)
        #     return
        print('*' * 10, '8', '*' * 10)
        print('[CONSUMER] Consuming %s...' % n)
        print('*' * 10, '3', '*' * 10)
        r = '200 OK'
        print('*' * 10, '7', '*' * 10)


def produce(c):
    print('*' * 10, '4', '*' * 10)
    c.send(None)
    n = 0
    print('*' * 10, '5', '*' * 10)
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('*' * 10, '9', '*' * 10)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
print('*' * 10, '6', '*' * 10)
produce(c)
