import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):

    # Read the image
    image = cv2.imread(image_path)

    # Check whether image is loaded
    if image is None:
        print("Error: Image not found!")
        return

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate histogram for Red channel
    red_hist = cv2.calcHist([image_rgb], [0], None, [256], [0, 256])

    # Calculate histogram for Green channel
    green_hist = cv2.calcHist([image_rgb], [1], None, [256], [0, 256])

    # Calculate histogram for Blue channel
    blue_hist = cv2.calcHist([image_rgb], [2], None, [256], [0, 256])

    # Create one window
    plt.figure(figsize=(10, 6))

    # Display original image
    plt.subplot(2, 1, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Display color histogram
    plt.subplot(2, 1, 2)

    plt.plot(red_hist, label="Red")
    plt.plot(green_hist, label="Green")
    plt.plot(blue_hist, label="Blue")

    plt.title("Color Histogram")
    plt.xlabel("Color Level (0-255)")
    plt.ylabel("Number of Pixels")

    plt.xlim([0, 256])
    plt.legend()

    plt.tight_layout()
    plt.show()


# Call the function
analyze_histogram("input 4.jpg")