class CsvReader():
	def	__init__(self, filename, sep = ',', isheader=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.isheader=isheader
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
	def	__enter__(self):
		try:
			self.file = open(self.filename, 'r')
		except:
			print(f"Error: {self.filename}; no such file")
			self.file = None
		return (self)
	def	__exit__(self,  exc_type, exc_val, exc_tb):
		if self.file:
			self.file.close()
	def	getdata(self):
		if self.file == None:
			self.data = None
			return None
		self.file_contents = self.file.read()
		lines = [line for line in self.file_contents.split("\n")]
		self.data = []
		for line in lines[self.skip_top:len(lines) - self.skip_bottom]:
			line_data = []
			for cell in line.split(self.sep):
				line_data.append(cell)
			self.data.append(line_data)
		self.header = self.data[0] if self.isheader else None
	def	get_header(self):
		return self.header


with CsvReader("aap.csv", ',', True, 0, 0) as file:
	file.getdata()
	if file.data:
		for line in file.data:
			for cell in line:
				print(cell)
		print(file.header)