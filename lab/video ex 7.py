import cv2

# --------------------------------------------------
# BASIC VIDEO PROCESSING
# Normal Motion, Slow Motion and Fast Motion
# --------------------------------------------------

# Read the captured video
video = cv2.VideoCapture("input.mp4")

# Check whether the video was opened successfully
if not video.isOpened():
    print("Error: Cannot open the video!")
    print("Make sure input.mp4 is in the same folder as video.py")
    exit()

print("Video opened successfully!")

print("-----------------------------------")
print("VIDEO PROCESSING")
print("-----------------------------------")
print("N = Normal Motion")
print("S = Slow Motion")
print("F = Fast Motion")
print("Q = Quit")
print("-----------------------------------")

# Default mode
mode = "normal"

while True:

    # Read one frame from the video
    ret, frame = video.read()

    # If video reaches the end, restart it
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Display the current mode on the video
    cv2.putText(
        frame,
        "Mode: " + mode,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display the video frame
    cv2.imshow("Video Processing", frame)

    # Set video speed
    if mode == "normal":
        delay = 30

    elif mode == "slow":
        delay = 100

    elif mode == "fast":
        delay = 1

    # Wait for keyboard input
    key = cv2.waitKey(delay) & 0xFF

    # Normal motion
    if key == ord("n"):
        mode = "normal"
        print("Normal motion selected")

    # Slow motion
    elif key == ord("s"):
        mode = "slow"
        print("Slow motion selected")

    # Fast motion
    elif key == ord("f"):
        mode = "fast"
        print("Fast motion selected")

    # Quit the program
    elif key == ord("q"):
        print("Video processing stopped")
        break

# Release the video
video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

print("Program completed successfully!")