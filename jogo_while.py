# Jogo pedra, papel e tesoura com loop while
from random import randint

novo = input('Vamos começar? s/n \n')
jog = 0
comp1 = 0

# loop while se novo for diferente de 'n' continue, se for igual a 'n' não entra em loop
while novo != 'n':
    # se jog igual 3 e comp1 menor que 3
    if jog == 3 and comp1 < 3:
        print('********************************************\n')
        print('VOCÊ GANHOU\n\n')
        print('********************************************\n')
        #print(f'JOGADOR {jog} COMPUTADOR {comp1}')
        novo = input('Uma nova partida? s/n \n')# voltando o inicio do loop
        jog = 0 # limpando jogador
        comp1 = 0 # limpando computador
    # senão comp1 igual 3 e jog menor que 3    
    elif comp1 == 3 and jog < 3:
        #print(f'JOGADOR {jog} COMPUTADOR {comp1}')
        print('********************************************\n')
        print('VOCÊ É UM PERDEDOR, HA HA HA HA HA\n\n')
        print('********************************************\n')
        novo = input('Uma nova partida? s/n \n')# voltando o inicio do loop
        jog = 0 # limpando jogador
        comp1 = 0 # limpando computador
    # começando o jogo
    else:
        print('\nEscolha:\nPedra = 1\nTesoura = 2\nPapel = 3')
        esc = int(input('\nQual a sua opção? \n'))
        comp = randint(1, 3)# opção do computador aleatório entre o 1 e 3

# se (esc igual a 1 e comp igual a 2) ou (esc igual a 2 e comp igual a 3) ou (esc igual a 3 e comp igual a 1)
        if (esc == 1 and comp == 2) or (esc == 2 and comp == 3) or (esc == 3 and comp == 1):
            print('---------------------------------------------------------------')
            print(f'Você escolheu {esc} e o computador {comp}, VOCÊ GANHOU !!!!!')
            print('---------------------------------------------------------------')
            jog += 1
            print(f'JOGADOR {jog} COMPUTADOR {comp1}')
# senão esc igual a comp
        elif esc == comp:
            print('---------------------------------------------------------------')
            print(f'Você escolheu {esc} e o computador {comp}, EMPATOU !!!!!')
            print('---------------------------------------------------------------')
            print(f'JOGADOR {jog} COMPUTADOR {comp1}')
        else:
            print('---------------------------------------------------------------')
            print(f'Você escolheu {esc} e o computador {comp}, VOCÊ PERDEU !!!!!')
            print('---------------------------------------------------------------')
            comp1 += 1
            print(f'JOGADOR {jog} COMPUTADOR {comp1}')   