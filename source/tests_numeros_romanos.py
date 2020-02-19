import unittest
import sys
from numeros_romanos import ConverteNumeroRomano

class TestConverteNumeroRomano(unittest.TestCase):
    
    def setUp(self):
        print("Contruir o objeto da class ConverteNumeroRomano")
        self.cnr = ConverteNumeroRomano()

    def tearDown(self):
        print("Destruir o objeto da class ConverteNumeroRomano")
        self.cnr = None
    
    @unittest.skipIf( sys.version_info > (2,7), "Não suporta versões superiores a 2.7")
    def test_mil(self):
        self.assertEqual(1000, self.cnr.converte_para_decimal('M'))

    def test_cem(self):        
        self.assertEqual(100, self.cnr.converte_para_decimal('C'))     

    def test_ciquenta(self):
        self.assertEqual(50, self.cnr.converte_para_decimal('L'))

    def test_vazio(self):        
        self.assertTrue(self.cnr.converte_para_decimal('') == 0)
        self.assertFalse(self.cnr.converte_para_decimal('') > 0)

if __name__ == '__main__':
    unittest.main()
