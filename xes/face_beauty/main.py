import xes.face_beauty.xes as xes
    
R = 128
G = 60
B = 200

W = 3
X = 15




#start = time.clock()
xes.imageupload()
xes.addColor(R,G,B)
xes.adjustWidth(W)
xes.skinWhiten(X)
xes.show()
#elapsed = (time.clock()-start)
#print('Time used: %f s'%elapsed)
