import unittest
from calculadora import Calculadora

class TddExemplo(unittest.TestCase):

    def teste_multi(self):
        calc = Calculadora()
        result = calc.multiplicar(20, 10)
        self.assertEqual(100, result)

	def teste_soma(self):
		calc = Calculadora()
		result = calc.somar(-20, 40)
		self.assertEqual(20, result)

	def teste_sub(self):
		calc = Calculadora()
		result = calc.subtrair(40, 20)
		self.assertEqual(20, result)


if __name__ == '__main__':
	unittest.main()