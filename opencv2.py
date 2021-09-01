import cv2 as cv
import numpy as np

# kernel=np.ones((5,5),np.uint8)
# img=cv.imread("lena.png")

# grayImg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blurImg=cv.GaussianBlur(grayImg,(7,7),0)
# imgCanny=cv.Canny(grayImg,100,100)
# imgDialation=cv.dilate(imgCanny,kernel,iterations=1)
# imgEroded=cv.erode(imgDialation,kernel,iterations=1)

# cv.imshow("grayImg",grayImg)
# cv.imshow("blurImg",blurImg)
# cv.imshow("imgCanny",imgCanny)
# cv.imshow("imgDialation",imgDialation)
# cv.imshow("imgEroded",imgEroded)

# cv.waitKey(0)
# cv.destroyAllWindows()

#--------------------------Resize--------------------------------

img=cv.imread("lena.png")
imgRe=cv.resize(img,(300,300))

cv.imshow("image2",imgRe)
cv.imshow("image",img)

print(img.shape)
print(imgRe.shape)
cv.dnn
cv.waitKey(0)
cv.destroyAllWindows()