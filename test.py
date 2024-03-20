import cv2
import matplotlib.pyplot as plt

# Set Matplotlib backend to Agg
plt.switch_backend('agg')

# Load the image
image = cv2.imread('./spidyAtDoffice.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(histogram, color='black')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram of Grayscale Image')

# Save the plot as an image file
plt.savefig('histogram.png')

# Close the plot
plt.close()
