import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Tracker Window")
cv2.createTrackbar("Hue min","Tracker Window",0,179,empty)
cv2.createTrackbar("Hue max","Tracker Window",179,179,empty)
cv2.createTrackbar("Sat min","Tracker Window",0,255,empty)
cv2.createTrackbar("Sat max","Tracker Window",255,255,empty)
cv2.createTrackbar("Val min","Tracker Window",0,255,empty)
cv2.createTrackbar("Val max","Tracker Window",255,255,empty)

while True:
    img = cv2.imread("lambo.png")
    img = cv2.resize(img,(600,400))
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min","Tracker Window")
    h_max = cv2.getTrackbarPos("Hue max","Tracker Window")
    s_min = cv2.getTrackbarPos("Sat min","Tracker Window")
    s_max = cv2.getTrackbarPos("Sat max","Tracker Window")
    v_min = cv2.getTrackbarPos("Val min","Tracker Window")
    v_max = cv2.getTrackbarPos("Val max","Tracker Window")
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    masks = cv2.inRange(img_hsv, lower, upper)
    img_result = cv2.bitwise_and(img,img,mask=masks)

    #print("Lower hue= ", lower,"Upper hue= ",upper)
    
    cv2.imshow("Original Image",img)
    cv2.imshow("Hue image",img_hsv)
    cv2.imshow("Mask image",masks)
    cv2.imshow("Bitwise",img_result)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.waitKey(0)