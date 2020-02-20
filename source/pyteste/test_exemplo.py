from my_math import multiplicar
from my_math import subtrair
from my_math import dividir
from my_math import somar

def test_multiplicar():
	assert multiplicar(10, 20) == 200

def test_sububtrair():
	assert subtrair(2, 3) == -1

def test_dividir():
	assert dividir(10, 5) == 2

def test_somar():
	assert somar(10, 20) == 30