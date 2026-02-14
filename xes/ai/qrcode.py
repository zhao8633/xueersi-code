from xes.ai.qrcodeTool.MyQR import myqr
import os
from PIL import Image
import xes.common.XesFileUpload
import xes.common.XesUtils as XesUtils
from urllib import request

has_upload = False
has_qrcode = False

def upload():
    global has_upload
    has_upload = True
    #默认空白地址，保证调用input在终端也能执行
    return 'http://haibian-wj-polar.oss-cn-beijing.aliyuncs.com/hufu-code/xes_live/lesson4-1.jpg'

def qrcode(text, *args):
    global has_qrcode
    has_qrcode = True
    if not check_contain_chinese(text):
        data = { 'type':'msg','desc':'友情提示','value' : '请输入全英文字符！' }
        XesUtils.InfoTransferAndExchange(data)
        data = { 'type':'xesexit','desc':'','value' : '请输入全英文字符！' }
        XesUtils.InfoTransferAndExchange(data)
        return

    if len(args)==0:
        myqr.run(
            words=text,
            version=4,
            level='H',
            colorized=True,
            save_name='pure_pic.png',#保存本地的名字
            save_dir=XesUtils.GetPath()
    	)
        final_pic_dir = XesUtils.GetPath()+'pure_pic.png'
        uploader = xes.common.XesFileUpload.XesFileUpload()
        oss_img_url = uploader.upload(final_pic_dir, 'png')
        data = { 'type':'result','desc':'生成的二维码链接:','value' : oss_img_url }
        XesUtils.InfoTransferAndExchange(data)
    elif len(args)==1:
        global has_upload
        if has_upload:
            img_src = XesUtils.GetArgByName('i','file',args[0])
        else:
            img_src = args[0]

        tmp_img_dir = XesUtils.GetPath()+'pictmp.jpg'
        request.urlretrieve(img_src,tmp_img_dir)
        myqr.run(
            words=text,
            version=4,
            picture=tmp_img_dir,
            colorized=True,
            save_name='mix_pic.png',#保存到本地的名字，写死
            save_dir=XesUtils.GetPath()
    	)
        final_pic_dir = XesUtils.GetPath()+'mix_pic.png'
        uploader = xes.common.XesFileUpload.XesFileUpload()
        oss_img_url = uploader.upload(final_pic_dir, 'png')
        data = { 'type':'result','desc':'生成的二维码链接:','value' : oss_img_url }
        XesUtils.InfoTransferAndExchange(data)
    else:
        data = { 'type':'msg','desc':'二维码生成失败，看看哪里出错了哟','value' : '' }
        XesUtils.InfoTransferAndExchange(data)


def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u0391' <= ch <= u'\uffe5':
            return False
    return True


hooks = XesUtils.ExitHooks()
hooks.hook()

def xesexit():
    # 是否是因为异常导致程序终止，如果终止就结束
    if hooks.exception is not None:
        # print("death by exception: %s" % hooks.exception)
        data = { 'type':'desc','desc':'系统发现程序异常:','value' : '请检查代码是否有错误，修复后再次尝试一下吧！' } 
        XesUtils.InfoTransferAndExchange(data)
        return
    if not has_qrcode:
        data = { 'type':'xesexit','desc':'','value' : '你没有使用qrcode函数哦' }
        XesUtils.InfoTransferAndExchange(data)

import atexit
atexit.register(xesexit)