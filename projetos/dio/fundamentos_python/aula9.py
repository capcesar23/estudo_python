'''
    Como gerar e escrever em um arquivo
    Como ler informações de um arquivo
    Como trabalhar com as informações dos arquivos
    Como trabalhar com Strings
    E mais um pouco sobre lambda
    Como copiar arquivo e mover arquivos
'''

# criando arquivo .txt e escrevendo
# pode fazer tambem com diretorio (~/home/cesar/python/projetos/dio)

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

# atualizando arquivo


def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

# ler arquivo


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    # escrever_arquivo('Primeiralinha.\n')
    # atualizar_arquivo('Terceira linha\n')
    ler_arquivo('teste.txt')
