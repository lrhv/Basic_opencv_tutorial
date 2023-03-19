import cv2 as cv

#--READING IMAGES-->

img = cv.imread('images/3.jpg')
cv.imshow('Dog', img)
cv.waitKey(0)

#--READING VIDEOS-->
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
     
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

