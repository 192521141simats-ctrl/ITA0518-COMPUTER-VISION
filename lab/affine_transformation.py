import cv2
import numpy as np

# Read the image
image = cv2.imread("input 13.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Define three points from the original image
points1 = np.float32([
    [50, 50],
    [width - 50, 50],
    [50, height - 50]
])

# Define three corresponding points for the transformed image
points2 = np.float32([
    [100, 80],
    [width - 100, 50],
    [80, height - 100]
])

# Create the affine transformation matrix
matrix = cv2.getAffineTransform(points1, points2)

# Apply affine transformation
transformed_image = cv2.warpAffine(
    image,
    matrix,
    (width, height)
)

# Display original image
cv2.imshow("Original Image", image)

# Display transformed image
cv2.imshow("Affine Transformed Image", transformed_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()