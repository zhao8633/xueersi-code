import xes.face_recognition.xes as xes
from xes.face_recognition.xes import layerfactory
import time

layer = layerfactory()

layer.first()
layer.second()
layer.third()

start = time.clock()
xes.facedetect()
elapsed = (time.clock() - start)
print("Time used: %f s" %elapsed)


#import numpy as np
#import urllib.request
#import cv2

#img_src = 'http://wx2.sinaimg.cn/mw690/ac38503ely1fesz8m0ov6j20qo140dix.jpg'
#resp = urllib.request.urlopen(img_src)
#image = np.asarray(bytearray(resp.read()), dtype="uint8")
#image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#cv2.imshow("Image", image)
#cv2.waitKey(0)




