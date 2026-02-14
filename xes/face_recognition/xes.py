#-*-coding:utf-8 -*-

import cv2
from xes.mtcnn.mtcnn import MTCNN
import numpy as np
import urllib.request
import cv2
import xes.common.XesFileUpload
import xes.common.XesUtils as XesUtils

g_xesexit = [False] # 是不是正常返回有用信息

g_flags = [False, False,False,False]
g_imgurl = ['']
def facedetect():
    if not (g_flags[0] and g_flags[1] and g_flags[2]) or g_flags[3]:
        return
    detector = MTCNN()
    img_src = 'http://wx2.sinaimg.cn/mw690/ac38503ely1fesz8m0ov6j20qo140dix.jpg' # 单个头像
    # img_src = 'http://pic22.photophoto.cn/20120317/0017029502053305_b.jpg' #风景画
    # img_src = 'http://dpic.tiankong.com/ut/pg/QJ6268374757.jpg?x-oss-process=style/670w' #多个头像

    # 获取命令行传入参数，没有使用默认值 
    img_src = XesUtils.GetArgByName('i','file',img_src)

    # print("识别前图片："+img_src)
    data = { 'type':'msg','desc':'识别前图片:','value' : img_src }
    XesUtils.InfoTransferAndExchange(data)

    resp = urllib.request.urlopen(img_src)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    result = detector.detect_faces(image)

    # Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
    if len(result)==1:
        bounding_box = result[0]['box']
        keypoints = result[0]['keypoints']
    
        cv2.rectangle(image,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (0, 155, 255),
                      5)
    
        cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

    elif len(result)==0:
        # print('该图像没有面部')
        data = { 'type':'msg','desc':'该图像没有面部:','value' : '上传一张带有人脸的图片试试吧！' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return
    else:
        # print('该图像有多个面部')
        data = { 'type':'msg','desc':'该图像有多个面部:','value' : '上传一张带有人一个脸的图片试试吧！' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return

    cv2.imwrite(XesUtils.GetPath()+"result-face-recognition.jpg", image)

    # 上传图片
    uploader = xes.common.XesFileUpload.XesFileUpload()
    imgurl = uploader.upload(XesUtils.GetPath()+"result-face-recognition.jpg", 'jpg')

    g_imgurl[0] = imgurl
    g_flags[3] = True


#def layerfactory()
class layerfactory:

    def edge(self):
        if g_flags[0]:
            return
        print('边缘检测OK - 第一层神经网络搭建完成')
        g_flags[0] = True
  
    def shape(slef):
        # 保证第1层网络OK
        if not g_flags[0] or g_flags[1]:
            return
        print('识别形状OK - 第二层神经网络搭建完成')
        g_flags[1] = True
        #g.buttonbox("第二层神经网络搭建完成",image = "neuro1.jpeg",choices = ("加油呀！继续搭第三层^_^"))

    def object(self):
        # 保证第2层网络OK
        if not g_flags[0] or not g_flags[1] or g_flags[2]:
            return
        print('识别对象OK - 第三层神经网络搭建完成')
        g_flags[2] = True
        #g.buttonbox("第三层神经网络搭建完成",image = "neuro1.jpeg",choices = ("搭建完成！"))


# 退出前回调

# type -- 显示第几题
def goodbye(type):
    if g_flags[0] == False:
        data = { 'type':'msg','desc':'第一层神经网络没有构建:','value' : '使用edge()构建一下第一层神经网络吧' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return

    if g_flags[1] == False:
        data = { 'type':'msg','desc':'第二层神经网络没有构建:','value' : '使用shape()构建一下第二层神经网络吧' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return

    if type == 'shape':
        data = { 'type':'result','desc':'识别后图片:','value' : 'https://xesfile.xesimg.com/programme/1539166455162.png' }
        XesUtils.InfoTransferAndExchange(data)
        data2 = { 'type':'msg','desc':'恭喜你!','value' : '小朋友，你太棒了！现在已经成功识别出人脸边缘和人脸形状，继续努力吧！' }
        XesUtils.InfoTransferAndExchange(data2)
        g_xesexit[0] = True
        return

    if g_flags[2] == False:
        data = { 'type':'msg','desc':'第三层神经网络没有构建:','value' : '使用object()构建一下第三层神经网络吧' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return

    if type == 'object':
        data = { 'type':'result','desc':'识别后图片:','value' : 'https://xesfile.xesimg.com/programme/1539166528796.png' }
        XesUtils.InfoTransferAndExchange(data)
        data2 = { 'type':'msg','desc':'恭喜你!','value' : '小朋友，你真厉害！现在已经成功识别出人脸边缘，人脸形状和人脸器官，继续加油吧！' }
        XesUtils.InfoTransferAndExchange(data2)
        g_xesexit[0] = True
        return

    if g_flags[3] == False and g_xesexit[0] == False:
        data = { 'type':'msg','desc':'facedetect()没有调用哦，快起完善一下代码吧！','value' : '' }
        XesUtils.InfoTransferAndExchange(data)
        g_xesexit[0] = True
        return

    # 图片异常已经返回提示了
    if g_flags[3] == False and g_xesexit[0] == True:
        return

    if type == 'all':
        data = { 'type':'result','desc':'识别后图片:','value' : g_imgurl[0] }
        XesUtils.InfoTransferAndExchange(data)
        data2 = { 'type':'msg','desc':'恭喜你!','value' : '小朋友，给你点赞！你已经成功的把图片中的人脸检测出来了，也成功掌握了人脸检测的知识。' }
        XesUtils.InfoTransferAndExchange(data2)
        g_xesexit[0] = True
        return



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
# atexit.register(xesexit, 'object')
# atexit.register(xesexit, 'shape')

        # # 识别形状 
        # data = { 'type':'msg','desc':'恭喜你!','value' : '小朋友，你太棒了！现在已经成功识别出人脸边缘和人脸形状，继续努力吧！' }
        # XesUtils.InfoTransferAndExchange(data)

        # # 识别物体
        # data = { 'type':'msg','desc':'恭喜你!','value' : '小朋友，你真厉害！现在已经成功识别出人脸边缘，人脸形状和人脸器官，继续加油吧！' }
        # XesUtils.InfoTransferAndExchange(data)

        # # 识别物体
        # data = { 'type':'msg','desc':'恭喜你!','value' : '小朋友，给你点赞！你已经成功的把图片中的人脸检测出来了，也成功掌握了人脸检测的知识。' }
        # XesUtils.InfoTransferAndExchange(data)