class Calculadora:
    def soma(self, valor_a, valor_b):
        return  valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


calculadora = Calculadora()

# quando for usar o método da classe tem que colocar o paranetese ao final 
print(calculadora.soma(10, 2))
print(calculadora.subtracao(10, 2))
print(calculadora.multiplicacao(10, 2))
print(calculadora.divisao(10, 2))

# class Calculadora:
#     def __init__(self):
#         pass

#     def soma(self, valor_a, valor_b):
#         return  valor_a + valor_b

#     def subtracao(self, valor_a, valor_b):
#         return valor_a - valor_b

#     def multiplicacao(self, valor_a, valor_b):
#         return valor_a * valor_b

#     def divisao(self, valor_a, valor_b):
#         return valor_a / valor_b
