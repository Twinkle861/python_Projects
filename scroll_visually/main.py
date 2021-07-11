

# control fb
# colour range as colour can vary due to lighting
# hsv=hue saturation value
# then mask it->pick only in given range
# not want noises/sikn color /color closes to yellow like orange
# get rid of fake things/noise=loop through contour and get their area
# noise have smaller area
# so select >300
# draw contour it is curve joining diff continous pts
# know position of this item=get bounding rect of contours
# to check if moving->diff in values of coordinates of consequtive
# run and open insta whenever move down press space ie scroll down

import cv2
import numpy as np
import pyautogui
import pyautogui

cap = cv2.VideoCapture(0)

yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])
prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
    for c in contours:
            area = cv2.contourArea(c)
            if area > 5000:
                print(f'Area: {area}')
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2 )
                # cv2.drawContours(frame, c, -1, (0, 255, 0), 2)
                print(f'Y coordinate: {y}')
                delta_y = abs(prev_y - y)
                print(delta_y)
                if delta_y > 20:
                    print('moving down')
                    pyautogui.press('space')  
                prev_y = y
            cv2.imshow('frame', frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 