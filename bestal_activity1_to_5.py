import os
from os.path import isfile
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

        plt.subplot(1, 3, 1)
        plt.plot(img1_hist_b, color="blue")
        plt.title("blue pixel from "+imgfile1)
        plt.xlabel("pixel value")
        plt.ylabel("frequency/quantity")

        plt.subplot(1, 3, 2)
        plt.plot(img1_hist_g, color="green")
        plt.title("green pixel")
        plt.xlabel("pixel value")
        plt.ylabel("frequency/quantity")

        plt.subplot(1, 3, 3)
        plt.plot(img1_hist_r, color="red")
        plt.title("red pixel")
        plt.xlabel("pixel value")
        plt.ylabel("frequency/quantity")

        plt.savefig('histogram_of_image_1.png')
        plt.close()

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 3, 1)
        plt.plot(img2_hist_b, color="blue")
        plt.title("blue pixel from "+imgfile2)
        plt.xlabel("pixel value")
        plt.ylabel("frequency/quantity")

        plt.subplot(1, 3, 2)
        plt.plot(img2_hist_g, color="green")
        plt.title("green pixel")
        plt.xlabel("pixel value")
        plt.ylabel("frequency/quantity")

        plt.subplot(1, 3, 3)
        plt.plot(img2_hist_r, color="red")
        plt.title("red pixel")
        plt.xlabel("pixel value")
        plt.ylabel("frequency/quantity")

        plt.tight_layout()
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

def activity4(imgfile: str) -> None:
    if os.path.isfile(imgfile):
        rgb_img = cv2.imread(imgfile)
        gry_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
        (_, bnw_img) = cv2.threshold(gry_img, 88, 255, cv2.THRESH_BINARY)
        his_gry_img = cv2.calcHist([gry_img], [0], None, [256], (0, 256))

        fig = plt.figure(figsize=(10, 5))

        ax1 = fig.add_subplot(221)
        ax1.imshow(cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB))
        ax1.set_title("orig RGB image")
        ax1.axis("off")

        ax2 = fig.add_subplot(222)
        ax2.imshow(gry_img, cmap='gray')
        ax2.set_title("grayscale of image")
        ax2.axis("off")

        ax3 = fig.add_subplot(223)
        ax3.imshow(bnw_img, cmap='gray')
        ax3.set_title("black and white")
        ax3.axis("off")

        ax4 = fig.add_subplot(224)
        ax4.plot(his_gry_img, color='black')
        ax4.set_xlabel("pixel value")
        ax4.set_ylabel("frequency")
        ax4.set_title("histogram of grayscale image")

        plt.tight_layout()
        plt.savefig("origRGB_grayScale_bnw_histogram.png")
        plt.close()

        cv2.imshow( "result activity 4", cv2.imread("./origRGB_grayScale_bnw_histogram.png") )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("image doesn't exist, or not the right dir")


# activity1("./pic/spidyAtDoffice.jpg")
# activity2("./spidyAtDoffice.jpg")
# activity3("./pic/spidyAtDoffice.jpg", "./pic/supernatural_004.png")
activity4("./pic/spidyAtDoffice.jpg")
