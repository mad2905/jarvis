# Import necessary libraries
import cv2
import numpy as np

# Load the ArUco dictionary
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# Create a parameter object
parameters = cv2.aruco.DetectorParameters_create()

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Load the image to superimpose (change the path to your image)
image = cv2.imread('nature.png')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect markers
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        for i in range(len(ids)):
            if ids[i] == 100:  # Change this to the marker ID you want to use
                # Draw a rectangle around the detected marker
                cv2.aruco.drawDetectedMarkers(frame, corners)

                # Get the transformation matrix
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs)

                # Superimpose the image onto the marker
                image_size = (image.shape[1], image.shape[0])
                img_warp = cv2.warpPerspective(image, np.linalg.inv(cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs)[0]), image_size)

                # Create a mask and place the superimposed image on it
                mask = np.zeros(frame.shape, dtype=frame.dtype)
                cv2.fillPoly(mask, corners.astype(int), (255, 255, 255))
                frame = cv2.bitwise_and(frame, cv2.bitwise_not(mask))
                frame += img_warp

    cv2.imshow('AR Application', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()