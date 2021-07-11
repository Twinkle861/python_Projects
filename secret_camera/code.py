import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2) #to capture diff or movement
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) #convert rgb to gray
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #blur it
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #get rid of unwanted things 
    dilated = cv2.dilate(thresh, None, iterations=3) #inc size of wanted things
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #creating frame like things
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) #create green rect
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Secret Camera', frame1)