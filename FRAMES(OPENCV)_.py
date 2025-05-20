import cv2

# read the image

image = cv2.imread("Images.png")
# resizeimage in frame
resizeimage = cv2.resize(image,(300,300))
# Blur image
blurimage = cv2.GaussianBlur(resizeimage,(5,5),5)
# Grayimage
grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
# edging image(detection)
edgeimage = cv2.Canny(resizeimage,threshold1=50,threshold2=80)
# display
cv2.imshow("Frame 1",image)
cv2.imshow("Frame 2",resizeimage)
cv2.imshow("Frame 3",blurimage)
cv2.imshow("Frame 4",grayimage)
cv2.imshow("Frame 5",edgeimage)
# compulsory until user closes display image
cv2.waitKey(0)
cv2.destroyAllWindows()

