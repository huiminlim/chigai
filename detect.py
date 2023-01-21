# Learnt from this Jupyter Notebook:
# https://github.com/jephraim-manansala/object-detection

import os

import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import match_template, peak_local_max
from skimage.io import imread, imshow

# Set directory path of current folder
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\data\\sample_2"
actual_image = f"{DATA_DIR}\\PXL_20230118_110244696.MP.jpg"
template_image = f"{DATA_DIR}\\template.jpg"
mask_image = f"{DATA_DIR}\\mask.jpg"

actual = cv2.imread(actual_image)
mask = cv2.imread(mask_image, 0)
actual = cv2.bitwise_and(actual, actual, mask=mask)
# cv2.imshow("", before)
# cv2.waitKey(1)

# before = imread(before_image)
actual_grey = rgb2gray(actual)
imshow(actual_grey)

template = imread(template_image)
template_grey = rgb2gray(template)
result = match_template(actual_grey, template_grey)

template_width, template_height = template_grey.shape
for x, y in peak_local_max(result, threshold_abs=0.5):
    rect = plt.Rectangle((y, x),
                         template_height,
                         template_width,
                         color='r',
                         fc='none')
    plt.gca().add_patch(rect)

output = f"{DATA_DIR}\\result.jpg"
plt.show()
plt.savefig(output)
