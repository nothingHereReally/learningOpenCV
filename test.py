import cv2
import numpy as np

img = cv2.imread("./spidyAtDoffice.jpg")
if img is None:
    print("image doesn't exist, or Atay, not the right dir")
else:
    cv2.imshow("spidy image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
