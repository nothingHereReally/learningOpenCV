from os.path import isfile
import cv2

imgfile: str = './pic/spidyAtDoffice.jpg'

if isfile(imgfile):
    image = cv2.imread(imgfile)
    width = image.shape[1]

    for i in range(image.shape[0]):
        for j in range( (i+9) % 10, width, 10):
            image[i, j] = [0, 0, 0]  # Set pixel to black

    cv2.imshow('Modified Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("file image does not exist: "+imgfile)

