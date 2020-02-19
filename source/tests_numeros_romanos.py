import unittest
from numeros_romanos import ConverteNumeroRomano

class TestConverteNumeroRomano(unittest.TestCase):
    
    def test_mil(self):
        value = ConverteNumeroRomano('M')
        self.assertEqual(1000, value.converte_para_decimal())

    def test_cem(self):
        value = ConverteNumeroRomano('C')
        self.assertEqual(100, value.converte_para_decimal())     

    def test_ciquenta(self):
        value = ConverteNumeroRomano('L')
        self.assertEqual(50, value.converte_para_decimal())

    def test_dez(self):
        value = ConverteNumeroRomano('X')
        self.assertEqual(10, value.converte_para_decimal())

    def test_vazio(self):
        value = ConverteNumeroRomano('')
        self.assertTrue(value.converte_para_decimal() == 0)
        self.assertFalse(value.converte_para_decimal() > 0)


if __name__ == '__main__':
    unittest.main()