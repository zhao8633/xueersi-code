import urllib
import numpy as np
import face_recognition
import os
from xes.mtcnn.mtcnn import MTCNN
from PIL import Image, ImageDraw

import xes.common.XesFileUpload
import xes.common.XesUtils as XesUtils

global d
global face_landmarks,pil_image
global index #标志位，用于确认是不是合规矩的图片

g_xesexit = [False] # 是不是正常返回有用信息
g_flags = [False, False,False,False,False]
g_imageuploadOK = [False]
g_imgurl = ['']

def imageupload():
#    File = 'Angelababy.jpg'
#    image = face_recognition.load_image_file(File)
    img_src = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1538300637312&di=a38f60aeb33a5502770b74e9626dba1b&imgtype=0&src=http%3A%2F%2F001.img.pu.sohu.com.cn%2Fgroup3%2FM03%2FFC%2FBA%2FMTAuMTAuODguODQ%3D%2FMTAwMTE0XzE1MTA5NjcyODU3MjE%3D%2Fcut%40m%3Dresize%2Cw%3D400%2Ch%3D400_cut%40m%3Dcrop%2Cx%3D0%2Cy%3D1%2Cw%3D399%2Ch%3D399.jpg'
#    img_src = 'http://pic22.photophoto.cn/20120317/0017029502053305_b.jpg' #风景画
#    img_src = 'http://dpic.tiankong.com/ut/pg/QJ6268374757.jpg?x-oss-process=style/670w' #多个头像
    # 获取命令行传入参数，没有使用默认值 
    img_src = XesUtils.GetArgByName('i','file',img_src)

    data = { 'type':'msg','desc':'识别前图片:','value' : img_src }
    XesUtils.InfoTransferAndExchange(data)

    g_imageuploadOK[0] = True

    r = urllib.request.urlopen(img_src)
    f = open(XesUtils.GetPath()+'haha.jpg', 'wb')
    f.write(r.read())
    f.close()
    image = Image.open(XesUtils.GetPath()+'haha.jpg') 

    image = image.convert('RGB')
    image = np.array(image)  
     
    # #查找图像中所有面部的所有面部特征
    # global face_landmarks,pil_image
    # face_landmarks_list = face_recognition.face_landmarks(image)
    # global index
    # global d
    # index = 1
    # if len(face_landmarks_list)==1:    
    #     face_landmarks = face_landmarks_list[0]
    # elif len(face_landmarks_list)==0:
    #     print('该图像没有面部')
    #     index = 0
    # else:
    #     print('该图像有多个面部')
    #     index = 0
    
    # pil_image = Image.fromarray(image)        
    # d = ImageDraw.Draw(pil_image, 'RGBA') 

    #查找图像中所有面部的所有面部特征
    global face_landmarks,pil_image
    face_landmarks_list = face_recognition.face_landmarks(image)    
    global index
    index = 1
    if len(face_landmarks_list)==1:    
        face_landmarks = face_landmarks_list[0]
    elif len(face_landmarks_list)==0:
        # print('该图像没有面部')
        data = { 'type':'msg','desc':'该图像没有面部:','value' : '上传一张带有人脸的图片试试吧！' }
        XesUtils.InfoTransferAndExchange(data)
        index = 0
        g_xesexit[0] = True
        return
    else:
        # print('该图像有多个面部')
        data = { 'type':'msg','desc':'该图像有多个面部:','value' : '上传一张带有人一个脸的图片试试吧！' }
        XesUtils.InfoTransferAndExchange(data)
        index = 0
        g_xesexit[0] = True
        return
    
    pil_image = Image.fromarray(image)
    
    global d
    d = ImageDraw.Draw(pil_image, 'RGBA')    

    data = { 'type':'msg','desc':'上传图片完成','value' : '' }
    XesUtils.InfoTransferAndExchange(data)
    g_flags[0] = True            
     

def addColor(R1,G1,B1):
    if g_flags[0] == False:
        return

    if index==1:
        global d
        if isinstance(R1,int) and R1>=0 and R1<=255 and\
        isinstance(G1,int) and G1>=0 and G1<=255 and\
        isinstance(B1,int) and B1>=0 and B1<=255:
            lipColor = (R1,G1,B1,256)
            d.polygon(face_landmarks['top_lip'], fill=lipColor)
            d.polygon(face_landmarks['bottom_lip'], fill=lipColor)
            
            g_flags[1] = True
        else:
            data = { 'type':'msg','desc':'在添加口红颜色中，请输入0到255之间的整数','value' : '' }
            XesUtils.InfoTransferAndExchange(data)
            g_xesexit[0] = True
            # print('请输入0到255之间的整数!')

def adjustWidth(W1):
    if g_flags[0] == False:
        return
    if index==1:
        global d 
        if isinstance(W1,int) and W1>=0 and W1<=10:
            eyeLineColor = (0,0,0,256)
            d.polygon(face_landmarks['left_eyebrow'], fill=eyeLineColor)
            d.polygon(face_landmarks['right_eyebrow'], fill=eyeLineColor)
            d.line(face_landmarks['left_eyebrow'], fill=eyeLineColor, width=W1)
            d.line(face_landmarks['right_eyebrow'], fill=eyeLineColor, width=W1)
            g_flags[2] = True
        else:
            # print('请输入0到10之间的整数!')
            data = { 'type':'msg','desc':'在调整眉毛宽度中，请输入0到10之间的整数','value' : '' }
            XesUtils.InfoTransferAndExchange(data)
            g_xesexit[0] = True

def skinWhiten(X1):
    if g_flags[0] == False:
        return
    if index==1:
        global pil_image 
        if isinstance(X1,int) and X1>=0 and X1<=100:
            X1 = (X1-50)/100
            print(X1)
            rgb2xyz = (1+X1,-X1/2,-X1/2,0,
                      -X1/2,1+X1,-X1/2,0,
                      -X1/2,-X1/2,1+X1,0)	
            pil_image = pil_image.convert("RGB", rgb2xyz)    
            rgb2xyz = (1-X1,0,0,0,
                      0,1-X1,0,0,
                      0,0,1-X1,0)
            pil_image = pil_image.convert("RGB", rgb2xyz)  

            g_flags[3] = True

        else:
            # print('请输入0到100之间的整数!') 
            data = { 'type':'msg','desc':'在调整美白中，请输入0到100之间的整数','value' : '' }
            XesUtils.InfoTransferAndExchange(data)
            g_xesexit[0] = True
            
    
def show():
    if g_xesexit[0] == True:
        return
    global pil_image
    img_path = XesUtils.GetPath()+'result-face-beauty.jpg'
    result = os.path.exists(XesUtils.GetPath())
    if result:
        pil_image.save(img_path,'jpeg')
        uploader = xes.common.XesFileUpload.XesFileUpload()
        img_path = XesUtils.GetPath()+'result-face-beauty.jpg'
        has_img = os.path.exists(img_path)
        if has_img :
            imgurl = uploader.upload(img_path, 'jpg')
            g_imgurl[0] = imgurl
            g_flags[4] = True
        else:
            data = { 'type':'msg','desc':'图片生成失败，请重试','value' : '' }
            XesUtils.InfoTransferAndExchange(data)
            g_xesexit[0] = True
    else:
        data = { 'type':'msg','desc':'图片生成失败，请重试','value' : '' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
    #pil_image.show()
    
    
# type -- 显示第几题
def goodbye(type):
    # 图片异常已经返回提示了
    if g_xesexit[0] == True:
        return

    if g_imageuploadOK[0] == False:
        data = { 'type':'msg','desc':'imageupload没有调用哦！','value' : '' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return

    if g_flags[4] == False:
        data = { 'type':'msg','desc':'程序结尾没有调用show()哦','value' : '' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return
    
    if g_flags[1] == True:
        data = { 'type':'msg','desc':'真厉害！','value' : '小朋友，你真厉害！涂上口红，变得更好看了呢！再接再厉！' }
        XesUtils.InfoTransferAndExchange(data)
    
    if g_flags[2] == True:
        data = { 'type':'msg','desc':'好棒哦!','value' : '小朋友，你好棒哦！修剪完眉毛，整个人都很自信了呢，继续最后一步美颜吧！' }
        XesUtils.InfoTransferAndExchange(data)

    if g_flags[3] == True:
        data = { 'type':'msg','desc':'666！','value' : '小朋友，666！我们又给照片美白了一下，非常棒！' }
        XesUtils.InfoTransferAndExchange(data)

    if g_flags[3] == True & g_flags[2] == True & g_flags[2] == True:
        data = { 'type':'msg','desc':'666！','value' : '小朋友，666！终于完成了全部的美颜，快分享给你的朋友们看一看吧！' }
        XesUtils.InfoTransferAndExchange(data)

    if g_flags[4] == True:
        data = { 'type':'result','desc':'识别后图片:','value' : g_imgurl[0] } 
        XesUtils.InfoTransferAndExchange(data)

    g_xesexit[0] = True


hooks = XesUtils.ExitHooks()
hooks.hook()

def xesexit(type):
    # 是否是因为异常导致程序终止，如果终止就结束
    if hooks.exception is not None:
        # print("death by exception: %s" % hooks.exception)
        data = { 'type':'desc','desc':'系统发现程序异常:','value' : '请检查代码是否有错误，修复后再次尝试一下吧！' } 
        XesUtils.InfoTransferAndExchange(data)
        return

    goodbye(type)
    if g_xesexit[0] == True :
        data = { 'type':'xesexit','desc':'正常退出啦','value' : '' }
        XesUtils.InfoTransferAndExchange(data)

import atexit
atexit.register(xesexit, 'all')






