__author__ = 'nickyuan'

#1、谈谈Python的装饰器、迭代器、yield
'''
    Python的装饰器decorator本质上可以说是一个闭包或者是命名空间，可以在不改变函数内部实现的同时为函数增加一些功能；
    比较常用的场景，比如说是日志管理、用户登录校验
    闭包函数必须有内嵌函数
    内嵌函数需要引用该嵌套函数上一级namespace中的变量
    闭包函数必须返回内嵌函数
    def greetingsConfig(prefix):
        def greetings(name):
            print(prefix, name)
        return greetings
    
    迭代器
    生成器就是generator，yield关键字实现，根据算法在循环的过程中不断计算出后续的元素，在每次迭代时返回一个值
    但是不需要创建list来保存，这样就可以节省大量的空间，只需要把【】改为（）就可以实现生成器
    gen = （x**2 for x in range(100)）
    
    生成器包含__iter() __next()函数
    可以通过generator.send(arg)来传入参数，这是协程模型
        
'''

#2、浅拷贝与深拷贝的区别、实现方式
'''
    浅拷贝通过
'''