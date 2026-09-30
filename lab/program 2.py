import cv2

# Read the image
image = cv2.imread("input1.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize image to fit the screen
image = cv2.resize(image, (800, 550))

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display original image
cv2.imshow("Original Butterfly Image", image)

# Display blurred image
cv2.imshow("Gaussian Blurred Image", blurred_image)

# Save the blurred image
cv2.imwrite("blurred_output.jpg", blurred_image)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()