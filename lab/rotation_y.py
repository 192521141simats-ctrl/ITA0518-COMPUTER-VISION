import cv2

# Read the image
image = cv2.imread("input 10.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Create rotation matrix for 90-degree clockwise rotation
center = (width // 2, height // 2)

matrix = cv2.getRotationMatrix2D(center, -90, 1.0)

# Perform rotation
rotated_image = cv2.warpAffine(image, matrix, (width, height))

# Display original image
cv2.imshow("Original Image", image)

# Display rotated image
cv2.imshow("90 Degree Clockwise Rotation", rotated_image)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()