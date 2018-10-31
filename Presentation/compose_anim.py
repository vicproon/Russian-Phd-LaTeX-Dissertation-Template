import cv2
import numpy as np

for i in range(1, 61):
    frame = cv2.imread('frame_%d.png' % i)
    slice_small = cv2.imread('slice_%d_small.png' % i)

    newim = np.zeros(shape=(275, 350 + 256, 3), dtype=np.uint8)
    newim[0:256, 0:256, :] = frame
    newim[:, 256:, :] = slice_small
    cv2.imwrite('composed_%d.png' % i, newim)