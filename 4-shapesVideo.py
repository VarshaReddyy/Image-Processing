import cv2 as cv
import datetime
cap=cv.VideoCapture('photos\cat_video.mp4')
while(cap.isOpened()):
    ret,frame =cap.read()
    frame=cv.resize(frame,(700,450))
    text=' Height: '+str(cap.get(4))+' Width: '+str(cap.get(3))
    date=" Date: "+str(datetime.datetime.now())
    frame=cv.rectangle(frame,(350,40),(200,200),(0,0,250),thickness=2)
    frame=cv.putText(frame,date,(10,20),1,1.1,(0,250,0),thickness=1)
    frame=cv.putText(frame,text,(10,40),1,1.1,(250,0,0),thickness=1)
    if ret==True:
        cv.imshow("frame",frame)
        if cv.waitKey(25) & 0xFF==ord("q"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()