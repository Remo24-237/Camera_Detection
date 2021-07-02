import cv2

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame_1 = cam.read() # recording first frame
    ret, frame_2 = cam.read() # recording second frame
    # Variable difference to hold the changes occurring between frames
    difference = cv2.absdiff(frame_1, frame_2)
    # converts the multi colored frame to a gray frame
    gray_color = cv2.cvtColor(difference,cv2.COLOR_RGB2GRAY)
    # removing unwanted noise in frame
    _, threshold = cv2.threshold(gray_color, 20, 255, cv2.THRESH_BINARY)

    # finding and drawing image contours in the frames
    contours, _ = cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c)<2000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame_1,(x,y), (x+w,y+h), (255,0,0),2)

    # used to define a variable to exit program
    if cv2.waitKey(10) == ord('q'):
        break
    # displays name in the top bar of the window
    cv2.imshow('My first camera', frame_1)