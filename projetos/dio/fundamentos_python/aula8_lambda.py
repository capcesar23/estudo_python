contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b


print(soma(5, 10))
print(subtracao(5, 10))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

print(f'A soma é: {soma(10 , 5)}')
print(f'A subtração é: {subtracao(10 , 5)}')
print(f'A multiplicação é: {multiplicacao(10 , 5)}')
print(f'A divisão é: {divisao(10 , 5)}')