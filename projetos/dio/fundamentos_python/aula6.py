'''
    o que é um conjunto
    Método de união
    Método intercecção
    Método de diferença
    Método de diferença simétrica
    Remoção de duplicidade de lista utilizando conjuntos
'''

conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print(f'União: {conjunto_uniao}') 
# União: {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_interseccao = conjunto.intersection(conjunto2)
print(f'Intercecção: {conjunto_interseccao}')
 # Intercecção: {5}
conjunto_diferenca = conjunto.difference(conjunto2)
print(f'Diferença entre 1 e 2: {conjunto_diferenca}')
 # Diferença entre 1 e 2: {1, 2, 3, 4}
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(f'Diferença entre 2 e 1: {conjunto_diferenca2}')
 # Diferença entre 2 e 1: {8, 6, 7}
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(f'Diferença simétrica: {conjunto_diff_simetrica}')
# Diferença simétrica: {1, 2, 3, 4, 6, 7, 8}

# conjunto = {1, 2, 3 ,4 ,4 ,2}
# conjunto.add(5) # adiciona o lemento dentro dele
# conjunto.discard(2) # exclui o elemento dele
# print(conjunto)