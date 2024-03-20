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
        # cv2.adaptiveThreshold(...)
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

        (img1_b, img1_g, img1_r) = cv2.split(img1)
        (img2_b, img2_g, img2_r) = cv2.split(img2)

        img1_hist_b = cv2.calcHist([img1_b], [0], None, [256], [0, 256])
        img1_hist_g = cv2.calcHist([img1_g], [0], None, [256], [0, 256])
        img1_hist_r = cv2.calcHist([img1_r], [0], None, [256], [0, 256])

        img2_hist_b = cv2.calcHist([img2_b], [0], None, [256], [0, 256])
        img2_hist_g = cv2.calcHist([img2_g], [0], None, [256], [0, 256])
        img2_hist_r = cv2.calcHist([img2_r], [0], None, [256], [0, 256])

        plt.figure(figsize=(10, 5))
        plt.plot(img1_hist_b, color="blue")
        plt.plot(img1_hist_g, color="green")
        plt.plot(img1_hist_r, color="red")

        plt.savefig('histogram_of_image_1.png')
        plt.close()

        plt.figure(figsize=(10, 5))
        plt.plot(img2_hist_b, color="blue")
        plt.plot(img2_hist_g, color="green")
        plt.plot(img2_hist_r, color="red")

        plt.savefig('histogram_of_image_2.png')
        plt.close()

        img1 = cv2.imread('./histogram_of_image_1.png')
        img2 = cv2.imread('./histogram_of_image_2.png')
        cv2.imshow("histogram of image 1", img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imshow("histogram of image 2", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



# activity1("./pic/spidyAtDoffice.jpg")
# activity2("./spidyAtDoffice.jpg")
activity3("./pic/spidyAtDoffice.jpg", "./pic/supernatural_004.png")
