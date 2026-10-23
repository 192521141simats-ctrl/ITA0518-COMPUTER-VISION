import cv2

# Read the image
image = cv2.imread("input 11.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Get the center of the image
center = (width // 2, height // 2)

# Create rotation matrix for 180-degree clockwise rotation
matrix = cv2.getRotationMatrix2D(center, -180, 1.0)

# Perform rotation
rotated_image = cv2.warpAffine(image, matrix, (width, height))

# Display original image
cv2.imshow("Original Image", image)

# Display rotated image
cv2.imshow("180 Degree Clockwise Rotation", rotated_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()