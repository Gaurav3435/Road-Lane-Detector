import cv2
import numpy as np
cap = cv2.VideoCapture("test_video.mp4") 

while(cap.isOpened()):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,500)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
    ret, img = cap.read()

    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,50,150,apertureSize = 3)
        
        lines = cv2.HoughLinesP(edges,1,np.pi/180,250,minLineLength=100,maxLineGap=10)
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()