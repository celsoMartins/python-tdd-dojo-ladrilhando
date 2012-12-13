from linha import Linha

class Quadrilatero:
	a1 = None
	a2 = None
	a3 = None
	a4 = None

	def __init__(self, a1, a2, a3, a4):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4

	def area(self):
		base = Linha(self.a1, self.a2)
		altura = Linha(self.a2, self.a3)
		return base.tamanho() * altura.tamanho()