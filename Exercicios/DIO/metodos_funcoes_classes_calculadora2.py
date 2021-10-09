
# Classes sem instanciar os objetos:
class Calculadora:
    # sempre que começar a classe ele passe pelo método init:

    def soma(self, valor_a, valor_b):  # sempre que chamar o método tem que retornar 2 valores / # return a + b
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(10, 2))
print(calculadora.divisao(100, 300))
print(calculadora.multiplicacao(2, 777))