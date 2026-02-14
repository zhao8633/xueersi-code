
import xes.common.XesUtils as XesUtils
import builtins


use_print = False
def print(str):
    # 协议
    global use_print
    use_print = True
    data = { 'type':'xesinner','desc':'','value' : str }
    XesUtils.InfoTransferAndExchange(data)
    return builtins.print(str)

hooks = XesUtils.ExitHooks()
hooks.hook()

def xesexit():
    # 是否是因为异常导致程序终止，如果终止就结束
    if hooks.exception is not None:
        # print("death by exception: %s" % hooks.exception)
        data = { 'type':'desc','desc':'系统发现程序异常:','value' : '请检查代码是否有错误，修复后再次尝试一下吧！' } 
        XesUtils.InfoTransferAndExchange(data)
        return
    if not use_print:
        data = { 'type':'xesexit','desc':'','value' : '你没有使用print函数哦' }
        XesUtils.InfoTransferAndExchange(data)

import atexit
atexit.register(xesexit)