import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("input1.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert BGR to RGB for displaying correctly
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display both images on the same page
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap="gray")
    plt.title("Gray Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()