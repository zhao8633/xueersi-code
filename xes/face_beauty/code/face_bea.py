# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:48:17 2018

@author: admin
"""





# filename : digital_makeup.py
# -*- coding: utf-8 -*-
# 导入pil模块 ，可用命令安装 apt-get install python-Imaging
from PIL import Image, ImageDraw
# 导入face_recogntion模块，可用命令安装 pip install face_recognition
import face_recognition
#将jpg文件加载到numpy数组中
import cv2
import numpy as np
import face



image = face_recognition.load_image_file(r"/Users/pangjia/Documents/MineMsJia/python/code/reba.jpeg")

#查找图像中所有面部的所有面部特征
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

#画眉
    d.polygon(face_landmarks['left_eyebrow'], fill=(137, 104, 89, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(137, 104, 89, 128))
    #d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=2)
    #d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=2)

#光泽的嘴唇
    d.polygon(face_landmarks['top_lip'], fill=(230, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(230, 0, 0, 128))
    #d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=3)
    #d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=3)

#闪耀眼睛
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

#涂一些眼线
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(130, 130, 130, 30), width=1)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(130, 130, 130, 30), width=1)


    #face.WhiteBeauty(pil_image,2)



    pil_image.show()
#美白
    #image = np.uint8(np.clip((20 * image + 10), 0, 255))
    #cv2.imshow('bai', white)
    #cv2.waitKey(0)

#磨皮
    #image = cv2.bilateralFilter(image, 0, 0, 10)


    #def Filter(image):
        # """
        # 色彩窗的半径
        # 图像将呈现类似于磨皮的效果
        # """
        # image：输入图像，可以是Mat类型，
        #       图像必须是8位或浮点型单通道、三通道的图像
        # 0：表示在过滤过程中每个像素邻域的直径范围，一般为0
        # 后面两个数字：空间高斯函数标准差，灰度值相似性标准差
        #image = cv2.imread(filepath)
        #image = cv2.bilateralFilter(image, 0, 0, 10)
        #cv2.imshow('filter', Remove)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()


    #    res = np.uint8(np.clip((1.2 * image + 10), 0, 255))
    #    tmp = np.hstack((dst, res))
    #    cv2.imshow('bai',res)

