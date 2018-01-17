import cv2
import numpy as np
from trackers import camshift


xs,ys,ws,hs = 0,0,0,0  #selection
xo,yo=0,0 #origin
selectObject = False
trackObject = 0
def onMouse(event, x, y, flags, prams):
    global xs,ys,ws,hs,selectObject,xo,yo,trackObject
    if selectObject == True:
        xs = min(x, xo)
        ys = min(y, yo)
        ws = abs(x-xo)
        hs = abs(y-yo)
    if event == cv2.EVENT_LBUTTONDOWN:
        xo,yo = x, y
        xs,ys,ws,hs= x, y, 0, 0
        selectObject = True
    elif event == cv2.EVENT_LBUTTONUP:
        selectObject = False
        trackObject = -1

cap = cv2.VideoCapture(0)
ret,frame = cap.read()
cv2.namedWindow('imshow')
cv2.setMouseCallback('imshow',onMouse)
while(True):
    ret,frame = cap.read()
    if trackObject != 0:
        trackwindow=(xs,ys,ws,hs)
        ret,trackwindow = camshift(frame,trackwindow,trackObject)
        trackObject = 1
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        cv2.polylines(frame,[pts],True, 255,2)

    if selectObject == True and ws>0 and hs>0:
        cv2.imshow('imshow1',frame[ys:ys+hs,xs:xs+ws])
        cv2.bitwise_not(frame[ys:ys+hs,xs:xs+ws],frame[ys:ys+hs,xs:xs+ws])
    cv2.imshow('imshow',frame)
    if  cv2.waitKey(100)==27:
        break
cv2.destroyAllWindows()