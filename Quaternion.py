class Quaternion(object):
	"""docstring for Quaternion"""
	def __add__(self, other):
		return Quaternion(self.h + other.h, 
			              self.i + other.i,
			              self.j + other.j,
			              self.k + other.k)

	def __init__(self, h=0, i=0, j=0, k=0):
		super(Quaternion, self).__init__()

		self.h = h
		self.i = i
		self.j = j
		self.k = k
		self.value = (self.h, self.i, self.j, self.k)


	def __repr__(self):
		return "Quaternion{}".format(self.value)

		