import os

import cv2

# Set directory path of current folder
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\data\\toy"

# Load video from path
video_path = f"{DATA_DIR}\\sample.mp4"
cap = cv2.VideoCapture(video_path)

# Extract first frame
cap.set(1, 1)
ret, frame = cap.read()
cv2.imshow("before", frame)
# cv2.waitKey(1)
cv2.imwrite(f"{DATA_DIR}\\before.jpg", frame)

# Extract last frame
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(total_frames)
cap.set(1, total_frames)
ret, frame = cap.read()
cv2.imshow("after", frame)
# cv2.waitKey(1)
cv2.imwrite(f"{DATA_DIR}\\after.jpg", frame)
