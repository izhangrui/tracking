import cv2
import numpy as np
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
def camshift(img, trackwindow, isFrist):
    (x,y,w,h)=trackwindow
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array((0., 30.,10.)), np.array((180.,256.,255.)))
    if isFrist == -1:
        hsv_roi = hsv[y:y+h,x:x+w]
        maskroi = mask[y:y+h,x:x+w]
        roi_hist = cv2.calcHist([hsv_roi],[0],maskroi,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    dst &=mask
    ret, trackwindow = cv2.CamShift(dst, trackwindow, term_crit)
    return ret, trackwindow


        



