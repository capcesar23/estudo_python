'''
    Condicional - Comando if
    Condicional - Comando else
    Condicional - Comando elif
    Operadores lógicos (and, or , not)
'''
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))

c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))

d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d)/4
print(f'A média é: {media}')

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print(f'A média é {media}')
# else:
#     print('Foi informado algum número errado')

# resto_a = a % 2
# resto_b = b % 2

# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')

# if a > b and a > c:
#     print(f'O maior número é: {a}')
# elif b > a and b > c:    
#     print(f'O maior número é: {b}')
# else:
#     print(f'O maior número é: {c}')