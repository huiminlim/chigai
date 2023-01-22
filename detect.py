# Learnt from this Jupyter Notebook:
# https://github.com/jephraim-manansala/object-detection

import os

import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import match_template, peak_local_max
from skimage.io import imread, imsave, imshow

# Set directory path of current folder
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\data\\sample_1"
actual_image = f"{DATA_DIR}\\PXL_20230118_110219929.MP.jpg"
template_image = f"{DATA_DIR}\\template.jpg"
mask_image = f"{DATA_DIR}\\mask.jpg"

actual = cv2.imread(actual_image)
mask = cv2.imread(mask_image, 0)
template = imread(template_image)

alpha = 1.2  # Contrast control (1.0-3.0)
beta = 0  # Brightness control (0-100)
actual = cv2.convertScaleAbs(actual, alpha=alpha, beta=beta)
template = cv2.convertScaleAbs(template, alpha=alpha, beta=beta)
actual = cv2.bitwise_and(actual, actual, mask=mask)
template_grey = rgb2gray(template)
imsave(f"{DATA_DIR}\\masked.png", actual)

actual_grey = rgb2gray(actual)
imshow(actual_grey)
result = match_template(actual_grey, template_grey)

template_width, template_height = template_grey.shape
points = []
for x, y in peak_local_max(result, threshold_abs=0.7):
    points.append([y, x])
points.sort()

for point in points:
    x = point[1]
    y = point[0]
    rect = plt.Rectangle((y+template_width//2, x+template_height//2),
                         5,
                         5,
                         color='r',
                         fc='none')
    plt.gca().add_patch(rect)

# Deduce the corner most point if it is not found
corner_x, corner_y = points[0][0], points[0][1] - template_height

with open(f"{DATA_DIR}\\output.txt", "w") as f:
    for [x, y] in points:
        f.writelines(f"{x} {y}\n")

with open(f"{DATA_DIR}\\corner.txt", "w") as f:
    f.writelines(f"{corner_x} {corner_y} {template_width} {template_height}")

plt.savefig(fname=f"{DATA_DIR}\\result.png", dpi=600)
# plt.show()
