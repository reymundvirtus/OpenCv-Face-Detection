import cv2

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # for face

while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # find faces in the frame
    for (x, y, w, h) in faces: # loop through the faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # then draw a rectangle in the faces
        reg_of_interest_gray = gray[y:y + w, x:x + w]
        reg_of_interest_color = frame[y:y + h, x:x + w]
        
    cv2.imshow('Frame', frame)

    # to quit press 'b'
    if cv2.waitKey(1) == ord('b'):
        break


capture.release()
cv2.destroyAllWindows()