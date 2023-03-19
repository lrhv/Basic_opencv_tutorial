import cv2 as cv

img = cv.imread('images/4.jpg')

cv.imshow('Dog', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)


cv.waitKey(0)

