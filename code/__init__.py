from face_landmark_detection import generate_face_correspondences
from delaunay_triangulation import make_delaunay
from face_morph import generate_morph_sequence

import subprocess
import argparse
import shutil
import os
import cv2

def doMorphing(img1, img2, duration, frame_rate, output):

	[size, img1, img2, points1, points2, list3] = generate_face_correspondences(img1, img2)

	tri = make_delaunay(size[1], size[0], list3, img1, img2)

	generate_morph_sequence(duration, frame_rate, img1, img2, points1, points2, tri, size, output)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--img1", required=True, help="The First Image")
	parser.add_argument("--img2", required=True, help="The Second Image")
	parser.add_argument("--duration", type=int, default=5, help="The duration")
	parser.add_argument("--frame", type=int, default=20, help="The frameame Rate")
	parser.add_argument("--output", help="Output Video Path")
	args = parser.parse_args()

	image1 = cv2.imread(args.img1)
	image2 = cv2.imread(args.img2)

	doMorphing(image1, image2, args.duration, args.frame, args.output)
	