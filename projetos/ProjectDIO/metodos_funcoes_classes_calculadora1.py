
# Como todos os métodos são cálculo, podemos criar uma classe chamada Calculadora:
class Calculadora:
    # sempre que começar a classe ele passe pelo método init:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    # Reaproveitamento de código:
    # Declarando um método:
    # def soma(a, b) :
    def soma(self):  # sempre que chamar o método tem que retornar 2 valores / # return a + b
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10,2)

    print(calculadora.valor_a)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())

# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(10, 2))
# print(divisao(10, 2))