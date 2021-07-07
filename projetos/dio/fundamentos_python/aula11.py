'''
    Como lançar uma exceção genérica
    Utilizar exceções especificas
    Encadeamento de exceções
    Else e Finally
    Criação de exceções customizadas
'''
# Tratamento de erro
# try:
#     divisao = 10 /0
# except ZeroDivisionError:
#     print('Não é possivel realizar divisão por 0!')
# except BaseException as ex:
#     print(f'Erro desconhecido. Erro {ex}')
# else:
#     print('Executa quando não oorre exceção')
# tudo que tá no finally dando erro ou não será executado
# finally:
#     print('Sempre executa')

# PERSONALIZANDO EXECEÇÃO
while True: # enquanto for verdade continue
    try:
         x = int(input('Digite um número'))
         print(x)
         break
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas número  ')