'''
    O que são métodos e funções
    Como declara métodos e funções
    Vantangens de se utilizar métodos e funções
    Como implementar class
    Vantangens de se utilizar classes
'''
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.valor_b)
# quando for usar o método da classe tem que colocar o paranete ao final 
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())

# def soma(self):
#         return self.valor_a + self.valor_b

# def subtracao(self):
#         return self.valor_a - self.valor_b

#     def multiplicacao(self):
#         return self.valor_a * self.valor_b

#     def divisao(self):
#         return self.valor_a / self.valor_b

# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(3, 4))
# print(multiplicacao(3, 4))
# print(divisao(3, 4))