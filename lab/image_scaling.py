import cv2

# Read the input image
image = cv2.imread("input 9.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Display original image
cv2.imshow("Original Image", image)

# Get original image size
height, width = image.shape[:2]

print("Original Width:", width)
print("Original Height:", height)

# Resize to bigger size
bigger_image = cv2.resize(
    image,
    (width * 2, height * 2),
    interpolation=cv2.INTER_LINEAR
)

# Resize to smaller size
smaller_image = cv2.resize(
    image,
    (width // 2, height // 2),
    interpolation=cv2.INTER_AREA
)

# Display bigger image
cv2.imshow("Bigger Image", bigger_image)

# Display smaller image
cv2.imshow("Smaller Image", smaller_image)

# Display resized image sizes
print("Bigger Image Width:", bigger_image.shape[1])
print("Bigger Image Height:", bigger_image.shape[0])

print("Smaller Image Width:", smaller_image.shape[1])
print("Smaller Image Height:", smaller_image.shape[0])

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()