import cv2
import matplotlib.pyplot as plt
import os

# Image file
image_path = "input 3.jpg"

print("Looking for image at:")
print(os.path.abspath(image_path))

# Read image
image = cv2.imread(image_path)

# Check image
if image is None:
    print("Error: Image not found!")
    print("Check the image name, extension, and folder.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Histogram equalization
equalized = cv2.equalizeHist(gray)

# Display images and histograms
plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(equalized, cmap="gray")
plt.title("Histogram Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.hist(gray.ravel(), 256, [0, 256])
plt.title("Original Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.subplot(2, 2, 4)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("Equalized Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()