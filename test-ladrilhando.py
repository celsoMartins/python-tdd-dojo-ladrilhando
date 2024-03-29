import unittest
from coordenada import Coordenada
from quadrilatero import Quadrilatero
from calculadora_ladrilho import CalculadoraLadrilho
from linha import Linha

class TesteLadrilhando(unittest.TestCase):
	
	# // TODO - Implementar teste
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

	def test_area_quadrilatero(self):
		a1 = Coordenada(0,0)
		a2 = Coordenada(2,0)
		a3 = Coordenada(2,2)
		a4 = Coordenada(0,2)

		ladrilho = Quadrilatero(a1, a2, a3, a4)
		area = ladrilho.area()
		self.assertEqual(ladrilho.area(), 4)

	def test_retornar_1_para_ladrilho_tamanho_comodo(self):
		a1 = Coordenada(0,0)
		a2 = Coordenada(2,0)
		a3 = Coordenada(2,2)
		a4 = Coordenada(0,2)

		ladrilho = Quadrilatero(a1, a2, a3, a4)
		comodo = Quadrilatero(a1, a2, a3, a4)
		calculadora = CalculadoraLadrilho(comodo, ladrilho)
		self.assertEqual(calculadora.calcularQtd(), 1)

	def test_retornar_4_para_ladrilho_metade_comodo(self):
		a1 = Coordenada(0,0)
		a2 = Coordenada(2,0)
		a3 = Coordenada(2,2)
		a4 = Coordenada(0,2)
		ladrilho = Quadrilatero(a1, a2, a3, a4)

		b1 = Coordenada(0,0)
		b2 = Coordenada(4,0)
		b3 = Coordenada(4,4)
		b4 = Coordenada(0,4)
		comodo = Quadrilatero(b1, b2, b3, b4)

		calculadora = CalculadoraLadrilho(comodo, ladrilho)
		self.assertEqual(calculadora.calcularQtd(), 4)

unittest.main()