import dis

def cond():
    x = 3
    if x < 5:
        return 'Yes'
    else:
        return "No"


print(cond.__code__.co_code)
print(list(bytearray(cond.__code__.co_code)))
print(dis.dis(cond()))
print(dis.opname[100])
'''可以看出输出分成5列。这5列分别指：

字节码对应的在源代码中的行号
该字节码在字节码串中的第几个字节，也就是该字节码的序号。
字节码的人类可读的名字
字节码参数
字节码参数的内容提示'''

'''一个指令加上它的参数一共占3个字节
帧包含了一段代码运行所需要的信息与上下文环境。
帧在代码执行时被动态地创建与销毁，每一个帧的创建对应一次函数调用，
所以每一个帧都有一个code object与其关联，同时一个code object可以拥有多个帧，
因为一个函数可以递归调用自己多次。'''

'''帧存在于调用栈中,你在程序异常时所看到的Traceback就是调用栈中的信息。
调用栈顾名思义就是每当你在当前函数内调用一次函数就在当前调用栈上压入所调用的函数的帧，
在所调用函数返回时再将该帧弹出。
这里再说下解释器用到的另外两个栈，第一个我们已经接触过了，
就是数据栈，执行字节码操作时使用的栈。
还有一个叫作块栈，用于特定的控制流，
比如循环与异常处理。每一个帧都拥有自己的数据栈与块栈。'''