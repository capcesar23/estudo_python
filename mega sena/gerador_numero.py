# simulador de sorteio da Mega Sena
# importar biblioteca random, serve para gerar números pseudoaleatórios e seu modulo randint para trazer números inteiros
from random import randint

sorteios = [ ]
contador = 1
# enquanto contador for menor ou igual a seis 6
while contador <= 6:
    numero = randint(1, 60)
    if not numero in sorteios: # se esse numero não estiver em sorteios adcione o numero
        sorteios.append(numero) # sorteios += 1
        contador += 1 
sorteios_crescente = sorted(sorteios)  # para retorna os numeros em ordem crescente     

print (sorteios_crescente)


