import cv2
from mtcnn.mtcnn import MTCNN
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import time
import easygui as g


def imageupload():
#if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #function to be called when mouse is clicked
    def printcoords():
        File = filedialog.askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
        filename = ImageTk.PhotoImage(Image.open(File))
        canvas.image = filename  # <--- keep reference of your image
        canvas.create_image(0,0,anchor='nw',image=filename)

    Button(root,text='choose',command=printcoords).pack()

    def autoClose():
        for i in range (6):

            time.sleep(6 - i)
        root.destroy()

    t = threading.Thread(target = autoClose)
    t.start()
    root.mainloop()



def facedetect(str):
    detector = MTCNN()

    imageinput = str
    image = cv2.imread(imageinput)

    result = detector.detect_faces(image)

    # Result is an array with all the bounding boxes detected. We know that for 'ivan.jpg' there is only one.
    bounding_box = result[0]['box']
    keypoints = result[0]['keypoints']

    cv2.rectangle(image,
                  (bounding_box[0], bounding_box[1]),
                  (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                  (0, 155, 255),
                  2)

    # cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
    # cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
    # cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
    # cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
    # cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

    cv2.imwrite("reba_jpeg.jpeg", image)

    # cv2.namedWindow("Image")
    cv2.imshow("reba_draw.jpeg", image)
    cv2.waitKey(0)

    print(result)


#def layerfactory()
class layerfactory:
    def first():
        print ("1")
        g.buttonbox("第一层神经网络搭建完成",image = "neuro1.jpeg",choices = ("加油呀！继续搭第二层^_^"))

    def second():
        print ("1")

    def third():
        print ("1")

    def fourth():
        print ("1")

    def five():
        print ("1")

