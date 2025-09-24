class Calculadora:

    LIMITE_MAXIMO = 9999999

    def soma(a, b):
        resultado = a + b
        Calculadora._verificar_overflow(resultado)
        return resultado

    def subtracao(a, b):
        resultado = a - b
        Calculadora._verificar_overflow(resultado)
        return resultado

    def multiplicacao(a, b):
        resultado = a * b
        Calculadora._verificar_overflow(resultado)
        return resultado

    def divisao(a, b):
        if b == 0:
            raise ZeroDivisionError("Erro: Divisão por zero")
        resultado = a / b
        Calculadora._verificar_overflow(resultado)
        return resultado
    
    def _verificar_overflow(valor):
        if abs(valor) > Calculadora.LIMITE_MAXIMO:
            raise OverflowError("Erro: Overflow")

