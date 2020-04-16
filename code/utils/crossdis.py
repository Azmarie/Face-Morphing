from __future__ import print_function
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--img1", required=True, help="The First Image")
parser.add_argument("--img2", required=True, help="The Second Image")
args = parser.parse_args()

src1 = cv2.imread(args.img1)
src2 = cv2.imread(args.img2)

alpha = 0.5
beta = (1.0 - alpha)
dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()