import os
import cv2
import matplotlib.pyplot as plt

plt.switch_backend('agg')

img = './pic/supernatural_004.png'
if os.path.exists(img):
    (img_b, img_g, img_r) = cv2.split(cv2.imread(img))
    print("img: ", img_b.shape)
    print("img: ", img_g.shape)
    print("img: ", img_r.shape)
    hist_b = cv2.calcHist([img_b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img_g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([img_r], [0], None, [256], [0, 256])
    plt.figure(figsize=(10, 5))

    # plt.subplot(1, 3, 1)
    plt.plot(hist_b, color='blue')

    # plt.subplot(1, 3, 2)
    plt.plot(hist_g, color='green')

    # plt.subplot(1, 3, 3)
    plt.plot(hist_r, color='red')

    # plt.tight_layout()
    plt.title('R(red color), G(green color), B(blue color)')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    plt.close()

    img = cv2.imread('./histogram.png')
    cv2.imshow("histogram", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("file doesn't exist")

