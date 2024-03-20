import cv2

def activity1(imgfile: str) -> None:
    img = cv2.imread(imgfile)
    if img is None:
        print("image doesn't exist, or not the right dir")
    else:
        # RGB show image
        cv2.imshow("spidy image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        imgInfo = img.shape
        print( "height: ", imgInfo[0] )
        print( "width: ", imgInfo[1] )
        print( "channels: ", imgInfo[2] )
        
        # RGB show pixel
        print( "pixel[ 0 ][ 0 ]( B, G, R ): ", img[0][0])
        
        # grayscale show image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("spidy image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        imgInfo = img.shape
        print("shape(height, width): ", imgInfo)

        # black and white show image
        (_, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow("spidy image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def activity2(imgfile: str) -> None:
    img = cv2.imread(imgfile)
    if img is None:
        print("image doesn't exist, or not the right dir")
    else:
        # size of an image
        imgInfo = img.shape
        print( "size of an image")
        print( "height: ", imgInfo[0] )
        print( "width: ", imgInfo[1] )

        # pixel sample of an image
        print("pixel[2][2]( B, G, R): ", img[2][2])

        # edges
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (_, img) = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
        cv2.imshow("spidy image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("pixel[44][44]( B, G, R): ", img[44][44])
        print("pixel[55][55]( B, G, R): ", img[55][55])



# activity1("./spidyAtDoffice.jpg")
# activity2("./spidyAtDoffice.jpg")
# activity2("./supernatural_004.png")
