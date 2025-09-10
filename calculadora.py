class Calculadora:

    def soma(a, b):
        resultado = a + b
        return resultado

    def subtracao(a, b):
        resultado = a - b
        return resultado

    def multiplicacao(a, b):
        resultado = a * b
        return resultado

    def divisao(a, b):
        if b == 0:
            raise ZeroDivisionError("Erro: Divisão por zero")
        resultado = a / b
        return resultado
