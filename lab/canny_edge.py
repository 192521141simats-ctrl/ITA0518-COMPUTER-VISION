import cv2

# Read the image
image = cv2.imread("input 3.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize image to fit the screen
image = cv2.resize(image, (800, 550))

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display original image
cv2.imshow("Original Butterfly Image", image)

# Display outline/edges
cv2.imshow("Canny Edge Detection", edges)

# Save the outline image
cv2.imwrite("canny_output.jpg", edges)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()