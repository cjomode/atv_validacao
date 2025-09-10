import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(Calculadora.soma(3, 2), 5)
        self.assertEqual(Calculadora.soma(-1, 1), 0)
        self.assertEqual(Calculadora.soma(-5, -7), -12)

    def test_subtracao(self):
        self.assertEqual(Calculadora.subtracao(10, 5), 5)
        self.assertEqual(Calculadora.subtracao(0, 5), -5)
        self.assertEqual(Calculadora.subtracao(-3, -2), -1)

    def test_multiplicacao(self):
        self.assertEqual(Calculadora.multiplicacao(4, 5), 20)
        self.assertEqual(Calculadora.multiplicacao(-2, 3), -6)
        self.assertEqual(Calculadora.multiplicacao(0, 100), 0)

    def test_divisao(self):
        self.assertEqual(Calculadora.divisao(10, 2), 5)
        self.assertEqual(Calculadora.divisao(-9, 3), -3)

        with self.assertRaises(ZeroDivisionError):
            Calculadora.divisao(5, 0)

if __name__ == '__main__':
    unittest.main()
