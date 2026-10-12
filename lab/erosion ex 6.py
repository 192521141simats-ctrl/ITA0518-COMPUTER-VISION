import cv2
import numpy as np
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Butterfly Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

# Check if a file was selected
if not image_path:
    print("No image selected!")
    exit()

# Read the selected image
image = cv2.imread(image_path)

# Check if image was loaded
if image is None:
    print("Error: Could not read the image!")
    exit()

print("Image loaded successfully!")
print("Image path:", image_path)
print("Image size:", image.shape)

# Create a small kernel
kernel = np.ones((3, 3), np.uint8)

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display original image
cv2.imshow("Original Image", image)

# Display eroded image
cv2.imshow("Eroded Image", eroded_image)

# Wait for key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()