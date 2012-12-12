import unittest
from coordenada import Coordenada
from comodo import Comodo
from ladrilho import Ladrilho
from calculadora_ladrilho import CalculadoraLadrilho

class TesteLadrilhando(unittest.TestCase):
	
	def test_1_ladrilho_para_comodo_do_tamanho_do_ladrilho(self):
		a1 = Coordenada(0,0)
		a2 = Coordenada(0,1)
		a3 = Coordenada(1,0)
		a4 = Coordenada(1,1)

		comodo = Comodo(a1, a2, a3, a4)
		ladrilho = Ladrilho(a1, a2, a3, a4)

		calculadoraLadrilho = CalculadoraLadrilho(comodo, ladrilho)
		self.assertEqual(calculadoraLadrilho.calcularQtd(), 1)

unittest.main()