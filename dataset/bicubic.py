import cv2
import glob
from PIL import Image

for filename in glob.glob('lowres/*.jpg'):
	print("Processing file: " + filename)
	image = cv2.imread(filename)
	res = cv2.resize(image,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
	cv2.imwrite(filename,res)
