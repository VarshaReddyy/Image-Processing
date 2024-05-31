import cv2 as cv

cap= cv.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        frame = cv.resize(frame,(700,450))
        grey= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow("grey",grey)
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF==ord("q"):
            break
cap.release()
cv.destroyAllWindows()
'''
cap= cv.VideoCapture('photos/cat_video.mp4')
while True:
    ret,frame=cap.read()
    frame = cv.resize(frame,(700,450))
    grey= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("grey",grey)
    cv.imshow("frame",frame)
    k= cv.waitKey(100)
    if k==ord(" "):
        break
cap.release()
cv.destroyAllWindows()
'''
