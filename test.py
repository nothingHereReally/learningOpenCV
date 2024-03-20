import cv2
import numpy as np

imgfile = "./spidyAtDoffice.jpg"
img = cv2.imread(imgfile)
if img is None:
    print("image doesn't exist, or Atay, not the right dir")
else:
    cv2.imshow("spidy image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    imgInfo = img.shape
    print( "height: ", imgInfo[0] )
    print( "width: ", imgInfo[1] )
    print( "channels: ", imgInfo[2] )

    print( "pixel[",int(img.shape[0]/2),"][",int(img.shape[1]/2),"]: ", img[int(img.shape[0]/2)][int(img.shape[1]/2)])
    print( "pixel[ 0 ][ 0 ]: ", img[0][0])

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("spidy image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    imgInfo = img.shape
    print("shape: ", imgInfo)
