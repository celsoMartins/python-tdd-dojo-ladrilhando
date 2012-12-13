import math

class Linha(object):

	a1 = None
	a2 = None

	def __init__(self, a1, a2):
		self.a1 = a1
		self.a2 = a2

	def tamanho(self):
		if self.a1.y == self.a2.y:
			return (self.a2.x - self.a1.x)
		elif self.a1.x == self.a2.x:
			return (self.a2.y - self.a1.y)
		else:
			parte1 = (self.a2.x - self.a1.x) ** 2
			parte2 = (self.a2.y - self.a1.y) ** 2
			return (math.sqrt(parte1 + parte2))