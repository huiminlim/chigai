import os

import cv2

# Set directory path of current folder
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\data"

# Load video from path
video_path = f"{DATA_DIR}\\sample.mp4"
cap = cv2.VideoCapture(video_path)

# Extract first frame
cap.set(1, 1)
ret, frame = cap.read()
cv2.imshow("", frame)
cv2.waitKey(0)

# Extract last frame
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
cap.set(1, total_frames)
ret, frame = cap.read()
cv2.imshow("", frame)
cv2.waitKey(0)
