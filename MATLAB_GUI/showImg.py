import cv2
import numpy as np
import sys

# Args
# [1] = images folder path
# [2] = test_type
# [3] = camera number
# [4] = number of images

imgFile = sys.argv[1] + '/' + sys.argv[2] + '/camera' + sys.argv[3] + '.raw'
nImgs = int(sys.argv[4])

with open(imgFile, 'rb') as f:
	raw_data = f.read()

image = np.frombuffer(raw_data, dtype=np.uint16)
if nImgs > 1:
	image = image.reshape(nImgs,800,1280)
else: 
	image = image.reshape(800,1280)

# image = cv2.imread(imgFile, cv2.IMREAD_ANYDEPTH)

if image is None:
	print("Image not found or couldn't be read.")
else:
	print("Max Image Intensity: {}".format(image.max()))
	#cv2.imshow("Image", image)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	
if nImgs > 1:
	for i in range(nImgs):
		cv2.imwrite(sys.argv[1] + '/' + sys.argv[2] + '/camera' + sys.argv[3] + '/' + f"{i:04d}" + '.tif', image[i,:,:])
else:
	cv2.imwrite(sys.argv[1] + '/' + sys.argv[2] + '/camera' + sys.argv[3] + '/0001' + '.tif', image[:,:])
