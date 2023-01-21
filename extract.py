# This program extracts first/last frames from video files
# and saves them out to image files
# Example arguments: python extract.py data/toy/sample.mp4 data/toy --backOffset 20

import argparse
import os

import cv2

parser = argparse.ArgumentParser(description='Extract video frames given the index numbers.')
parser.add_argument("videopath", type=str, help="Get video file path")
parser.add_argument("outputdir", type=str, help="Directory to save output images")
parser.add_argument("--backOffset", type=int, help="Offset number of frames counting from back", default=0)
args = parser.parse_args()

# Load video from path
if os.path.exists(args.videopath):
    cap = cv2.VideoCapture(args.videopath)
else:
    raise Exception(f"File {args.videopath} does not exist")

# Extract first frame
cap.set(1, 1)
ret, frame = cap.read()
# cv2.imshow("before", frame)
# cv2.waitKey(1)
cv2.imwrite(f"{args.outputdir}\\before.jpg", frame)

# Extract last frame
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
if total_frames - args.backOffset > 0:
    cap.set(1, total_frames - args.backOffset)
    ret, frame = cap.read()
    # cv2.imshow("after", frame)
    # cv2.waitKey(1)
    cv2.imwrite(f"{args.outputdir}\\after.jpg", frame)
else:
    raise Exception("Last frame is invalid")
