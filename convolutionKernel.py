import cv2
import numpy
import sys
import math

def gaussian(x, y, sigma):
	return 1/(2 * math.pi * (sigma**2)) * math.exp(-(x**2 + y**2)/(2*(sigma**2)))
def gaussianBlurKernel(kernelSize, sigma):
	convolutionKernel = numpy.empty((kernelSize, kernelSize))
	for i in range(kernelSize):
		for j in range(kernelSize):
			x = i - math.floor(kernelSize/2)
			y = j - math.floor(kernelSize/2)
			convolutionKernel[i, j] = gaussian(x, y, sigma)
	return convolutionKernel

# Read arguments (image filename and kernel entries)
filename = sys.argv[1]
kernelArguments = sys.argv[2:]

# Load image
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

# Construct convolution kernel
convolutionKernel = None
if (kernelArguments[0] == "box-blur"):
	kernelSizeFloat = float(kernelArguments[1])
	kernelSize = int(kernelSizeFloat)
	if (kernelSize != kernelSizeFloat or kernelSize < 1):
		sys.exit("Kernel size must be a natural number")

	convolutionKernel = numpy.ones((kernelSize, kernelSize))
elif (kernelArguments[0] == "normalized-box-blur"):
	kernelSizeFloat = float(kernelArguments[1])
	kernelSize = int(kernelSizeFloat)
	if (kernelSize != kernelSizeFloat or kernelSize < 1):
		sys.exit("Kernel size must be a natural number")

	entryValue = 1 / (kernelSize ** 2)
	convolutionKernel = numpy.full((kernelSize, kernelSize), entryValue)
elif (kernelArguments[0] == "gaussian-blur"):
	sigma = float(kernelArguments[2])
	kernelSizeFloat = float(kernelArguments[1])
	kernelSize = int(kernelSizeFloat)
	if (kernelSize != kernelSizeFloat or kernelSize < 1):
		sys.exit("Kernel size must be a natural number")

	convolutionKernel = gaussianBlurKernel(kernelSize, sigma)
elif (kernelArguments[0] == "normalized-gaussian-blur"):
	sigma = float(kernelArguments[2])
	kernelSizeFloat = float(kernelArguments[1])
	kernelSize = int(kernelSizeFloat)
	if (kernelSize != kernelSizeFloat or kernelSize < 1):
		sys.exit("Kernel size must be a natural number")

	convolutionKernel = gaussianBlurKernel(kernelSize, sigma)
	entrySum = 0
	for i in range(kernelSize):
		for j in range(kernelSize):
			entrySum += convolutionKernel[i, j]
	for i in range(kernelSize):
		for j in range(kernelSize):
			convolutionKernel[i, j] /= entrySum
else:
	kernelSizeFloat = math.sqrt(len(kernelArguments))
	kernelSize = int(kernelSizeFloat)
	if (kernelSize == 0 or (kernelSize != kernelSizeFloat)):
		sys.exit("Kernel must be square")
	convolutionKernel = numpy.empty((kernelSize, kernelSize))
	for i, n in enumerate(kernelArguments):
		convolutionKernel[math.floor(i / kernelSize), i % kernelSize] = n
print("Convolution kernel:")
print(convolutionKernel)

# Apply convolution kernel
convolutedImage = cv2.filter2D(image, -1, convolutionKernel)

# GUI
# 	S: Save
#	X: Close window
cv2.imshow("Original image", image)
cv2.imshow("Applied convolution kernel", convolutedImage)
key = None
while (key != 0x78):
	key = cv2.waitKey(0)
	if (key == 0x73):
		cv2.imwrite("appliedConvolutionKernel.png", convolutedImage)
cv2.destroyAllWindows()