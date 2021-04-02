import unittest
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retonar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retonar_0(self):
        self.assertEqual(soma(-5, 5), 0)


unittest.main(verbosity=2)
