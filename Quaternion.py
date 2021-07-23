class Quaternion(object):
	"""docstring for Quaternion"""
	def __init__(self, h, i, j, k):
		super(Quaternion, self).__init__()

		self.h = h
		self.i = i
		self.j = j
		self.k = k
		self.value = (self.h, self.i, self.j, self.k)


	def __repr__(self):
		return "Quaternion{}".format(self.value)

		