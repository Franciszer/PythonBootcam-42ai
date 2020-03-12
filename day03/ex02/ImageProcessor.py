import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ImageProcessor:
	@staticmethod
	def	load(path):
		return mpimg.imread(path)
	@staticmethod
	def	display(array):
		plt.imshow(array)
		plt.show()
