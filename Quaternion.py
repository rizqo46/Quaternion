class Quaternion(object):
	"""docstring for Quaternion"""
	def __neg__(self):
		return Quaternion(-self.h, -self.i, -self.j, -self.k)
		
	def __mul__(self, other):
		a = self
		b = other

		h = a.h*b.h - a.i*b.i - a.j*b.j - a.k*b.k
		i = a.h*b.i + a.i*b.h + a.j*b.k - a.k*b.j
		j = a.h*b.j - a.i*b.k + a.j*b.h + a.k*b.i
		k = a.h*b.k + a.i*b.j - a.j*b.i + a.k*b.h

		return Quaternion(h, i ,j ,k)

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

		