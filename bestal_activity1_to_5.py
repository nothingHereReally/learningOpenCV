import cv2
import matplotlib.pyplot as plt

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

def activity3(imgfile1: str, imgfile2: str) -> None:
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)
    if img1 is None and img2 is None:
        print("image doesn't exist, or not the right dir")
    else:
        pass
        cv2.imshow("image 1", img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imshow("image 2", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        histg1 = cv2.calcHist([gray_img1], [0], None, [256], [0, 256])
        histg2 = cv2.calcHist([gray_img2], [0], None, [256], [0, 256])
        plt.plot(histg1, color='black')
        # plt.plot(histg2, color='red')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of Grayscale Image')
        plt.show()


# activity1("./spidyAtDoffice.jpg")
# activity2("./spidyAtDoffice.jpg")
activity3("./spidyAtDoffice.jpg", "./supernatural_004.png")
