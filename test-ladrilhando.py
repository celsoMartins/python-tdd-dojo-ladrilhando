import unittest
from coordenada import Coordenada
from comodo import Comodo
from ladrilho import Ladrilho
from calculadora_ladrilho import CalculadoraLadrilho
from linha import Linha

class TesteLadrilhando(unittest.TestCase):
	
	# //TODO - Implementar teste
	# def test_nao_aceitar_ponto2_menor_que_ponto1(self):

	def test_tamanho_linha_horizontal(self):
		a1 = Coordenada(2,1)
		a2 = Coordenada(5,1)
		linha = Linha(a1, a2)
		self.assertEqual(linha.tamanho(), 3)

	def test_tamanho_linha_vertical(self):
		a1 = Coordenada(1, 2)
		a2 = Coordenada(1, 5)
		linha = Linha(a1, a2)
		self.assertEqual(linha.tamanho(), 3)

	def test_tamanho_linha_diagonal(self):
		a1 = Coordenada(1, 3)
		a2 = Coordenada(8, 11)
		linha = Linha(a1, a2)
		self.assertEqual(linha.tamanho(), 10.63014581273465)

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