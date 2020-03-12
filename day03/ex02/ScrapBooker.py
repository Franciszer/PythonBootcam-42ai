from ImageProcessor import ImageProcessor
from NumPyCreator import NumPyCreator
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class	ScrapBooker:
	#crop(array, dimensions, position) : crops the image as a rectangle with the given dimensions 
	# (meaning, the new height and width for the image), whose top left corner is given by the position argument. 
	# The position should be (0,0) by default. You have to consider it an error (and handle said error)
	#if dimensions is larger than the current image size.
	@staticmethod
	def	crop(array, dimensions, position = (0,0)):
		size = array.shape
		print(size[1] + position[0], size[0] + position[1])
		if size[1] < dimensions[0] + position[0] or size[0] < dimensions[1] + position[1]:
			print("ERROR: crop")
			exit()
		return (array[position[0]:dimensions[0] + position[0], position[1]:dimensions[1] + position[1]])
	@staticmethod
	def	thin(array, n, axis):
		for i in range(0, )

img = ImageProcessor.load("dices.png")
img = ScrapBooker.crop(img, (700,300), (100,301))
ImageProcessor.display(img)