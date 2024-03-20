import os
import cv2
import matplotlib.pyplot as plt

plt.switch_backend('agg')

img = './pic/supernatural_004.png'
if os.path.exists(img):
    img = cv2.imread(img)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    plt.plot(histogram, color='black')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Grayscale Image')

    # Save the plot as an image file
    plt.savefig('histogram.png')

    # Close the plot
    plt.close()
else:
    print("file doesn't exist")

