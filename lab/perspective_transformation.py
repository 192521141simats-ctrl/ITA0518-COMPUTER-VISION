import cv2
import numpy as np

# Read the image
image = cv2.imread("input 14.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Define four points in the original image
points1 = np.float32([
    [50, 50],
    [width - 50, 50],
    [width - 50, height - 50],
    [50, height - 50]
])

# Define four corresponding points for the output image
points2 = np.float32([
    [0, 0],
    [width, 0],
    [width, height],
    [0, height]
])

# Create perspective transformation matrix
matrix = cv2.getPerspectiveTransform(points1, points2)

# Apply perspective transformation
transformed_image = cv2.warpPerspective(
    image,
    matrix,
    (width, height)
)

# Display original image
cv2.imshow("Original Image", image)

# Display perspective transformed image
cv2.imshow("Perspective Transformed Image", transformed_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()