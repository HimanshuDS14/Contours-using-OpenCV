import cv2

image = cv2.imread("tom.jpg")

gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

ret , thresh = cv2.threshold(gray_image , 127,255 , cv2.THRESH_BINARY)

countours , hierarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)

print(str(len(countours)))

cv2.drawContours(image , countours , -1 , (0,0,255,5))



cv2.imshow("image" , image)
cv2.imshow("gray" , gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()