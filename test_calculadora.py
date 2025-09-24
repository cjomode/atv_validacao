import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        #partição de equivalência
        self.assertEqual(Calculadora.soma(3, 2), 5) #positivos
        self.assertEqual(Calculadora.soma(-1, 1), 0) #positivo e negativo
        self.assertEqual(Calculadora.soma(-5, -7), -12) #negativos
        self.assertEqual(Calculadora.soma(5.5, 2.3),7.8) #decimais

    def test_subtracao(self):
        self.assertEqual(Calculadora.subtracao(10, 5), 5)
        self.assertEqual(Calculadora.subtracao(0, 5), -5)
        self.assertEqual(Calculadora.subtracao(-3, -2), -1)
        self.assertEqual(Calculadora.subtracao(9.1,2.1),7)

    def test_multiplicacao(self):
        self.assertEqual(Calculadora.multiplicacao(4, 5), 20)
        self.assertEqual(Calculadora.multiplicacao(-2, 3), -6)
        self.assertEqual(Calculadora.multiplicacao(0, 100), 0)
        self.assertEqual(Calculadora.multiplicacao(7.8,1.6),12.48)

    def test_divisao(self):
        self.assertEqual(Calculadora.divisao(10, 2), 5)
        self.assertEqual(Calculadora.divisao(-9, 3), -3)

        with self.assertRaises(ZeroDivisionError):
            Calculadora.divisao(5, 0)

    def test_valor_limite(self):
        self.assertEqual(Calculadora.soma(9999990, 9), 9999999)  #limite
        with self.assertRaises(OverflowError):
            Calculadora.soma(9999999, 9999999 + 1)  #ultrapassa o limite

    def test_tabela_decisao(self):
        self.assertEqual(Calculadora.soma(15, 0), 15)

    #Transição de Estados 
    def test_transicao_estados(self):
        resultado = Calculadora.soma(5, 5)     #estado inicial
        resultado = Calculadora.multiplicacao(resultado, 2)  #novo estado
        resultado = Calculadora.subtracao(resultado, 5)  #transição
        self.assertEqual(resultado, 15)


if __name__ == '__main__':
    unittest.main()
