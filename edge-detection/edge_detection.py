"""
Loads and displays a video.
"""

# Importing OpenCV
import cv2
import numpy as np
import imutils
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read the video
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Converting the image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Smoothing without removing edges.
        gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)

        # Applying the canny filter
        edges = cv2.Canny(gray, 60, 120)
        edges_filtered = cv2.Canny(gray_filtered, 60, 120)

        # Stacking the images to print them together for comparison
        images = np.hstack((gray, edges, edges_filtered))

        #frame = imutils.resize(frame, width=1600, height=800)

        # Display the resulting frame
        cv2.imshow('Frame', images)
        # cv2.imshow('Frame', gray)
        # cv2.imshow('Frame', edges)
        # cv2.imshow('Frame', edges_filtered)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()