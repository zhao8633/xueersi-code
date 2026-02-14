import cv2
cap = cv2.VideoCapture(img_src)
if( cap.isOpened() ) :
    ret,img = cap.read()
    cv2.imshow("image",img)
    cv2.waitKey()


import numpy as np
import urllib
import cv2
resp = urllib.urlopen(img_src)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow("Image", image)
cv2.waitKey(0)

