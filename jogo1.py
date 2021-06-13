# Jogo pedra, papel e tesoura
from random import randint

print('Escolha:\nPedra = 1\nTesoura = 2\nPapel = 3')

esc = int(input('Qual a sua opção? '))
comp = randint(1,3)
# se (esc igual a 1 e comp igual a 2) ou (esc igual a 2 e comp igual a 3) ou (esc igual a 3 e comp igual a 1)
if (esc == 1 and comp == 2) or (esc == 2 and comp == 3) or (esc == 3 and comp == 1):
    print('---------------------------------------------------------------')
    print(f'Você escolheu {esc} e o computador {comp}, VOCÊ GANHOU !!!!!')
    print('---------------------------------------------------------------')    
# senão esc igual a comp
elif esc == comp:
    print('---------------------------------------------------------------')
    print(f'Você escolheu {esc} e o computador {comp}, EMPATOU !!!!!')
    print('---------------------------------------------------------------')
else:
    print('---------------------------------------------------------------')
    print(f'Você escolheu {esc} e o computador {comp}, VOCÊ PERDEU !!!!!')
    print('---------------------------------------------------------------')   
    