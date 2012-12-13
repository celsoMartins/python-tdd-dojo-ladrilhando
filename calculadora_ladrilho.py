class CalculadoraLadrilho:

	comodo = None
	ladrilho = None

	def __init__(self, comodo, ladrilho):
		self.comodo = comodo
		self.ladrilho = ladrilho

	def calcularQtd(self):
		qtdLadrilhos = self.comodo.area() / self.ladrilho.area()
		return qtdLadrilhos