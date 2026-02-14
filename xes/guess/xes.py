from random import *
import builtins
import xes.common.XesUtils as XesUtils


times = 0
number =   - 1

def input():
    while True:
        number = builtins.input()
        try:
            x = eval(number)
            if type(x) == int:
                global times
                times += 1
                return x
        except:
            data = { 'type':'desc','desc':'系统发现程序异常:','value' : '请输入一个数字' } 
            XesUtils.InfoTransferAndExchange(data)

        

    
    


hooks = XesUtils.ExitHooks()
hooks.hook()

def xesexit():
    # 是否是因为异常导致程序终止，如果终止就结束
    if hooks.exception is not None:
        # print("death by exception: %s" % hooks.exception)
        data = { 'type':'desc','desc':'系统发现程序异常:','value' : '请检查代码是否有错误，修复后再次尝试一下吧！' } 
        XesUtils.InfoTransferAndExchange(data)
        return
    
    data = { 'type':'xesexit','desc':'#尝试次数#你一共猜了' + str(times)+'次','value' : '' }
    XesUtils.InfoTransferAndExchange(data)


import atexit
atexit.register(xesexit)