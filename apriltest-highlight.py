# from this guide: https://pyimagesearch.com/2020/11/02/apriltag-with-python/
import cv2
import numpy as np
from apriltag import Detector, DetectorOptions
# test

# some helpful functions
def get_distance():
    """Inputs: (tag) detection size, Outputs: Distance (meters)"""
    # Get the center point of the detection
    center = (detection.center[0], detection.center[1])

    # Calculate the distance to the tag using the size of the tag in the image
   
    fx = intrinsic_matrix[0, 0]
    tag_size = 0.152  # size of AprilTag in meters
    focal_length = fx
    distance = tag_size * focal_length / detection.size


# Initialize the AprilTag detector with correct family for FRC tags
options = DetectorOptions(families="tag16h5")
detector = Detector(options)

# Initialize the camera
 
camera = cv2.VideoCapture(0)

while True:
    # Capture the image from camera
    ret, frame = camera.read()

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect tags
    print("[INFO] detecting AprilTags...")
    detections = detector.detect(gray) 
    print("[INFO] {} total AprilTags detected".format(len(detections)))

    # loop over the AprilTag detection results
    for detection in detections:
        # extract the bounding box (x, y)-coordinates for the AprilTag
        # and convert each of the (x, y)-coordinate pairs to integers
        (ptA, ptB, ptC, ptD) = detection.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))

        # draw the bounding box of the AprilTag detection
        cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
        cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
        cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
        cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

        # draw the center (x, y)-coordinates of the AprilTag
        (cX, cY) = (int(detection.center[0]), int(detection.center[1]))
        cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

        # draw the tag family on the image
        tagFamily = detection.tag_family.decode("utf-8")
        cv2.putText(frame, tagFamily, (ptA[0], ptA[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print("[INFO] tag family: {}".format(tagFamily))
        #distance test print
        get_distance()
        print(distance)

        

    # show the output image after AprilTag detection
    cv2.imshow("frame", frame)
    # Check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the Raspberry Pi camera
camera.release()

# Close all windows
cv2.destroyAllWindows()
