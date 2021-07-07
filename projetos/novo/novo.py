import requests

response = requests.get('https://viacep.com.br/ws/72880706/json/')
#print(response.status_code)
#print(response.json())
dados_cep = response.json()
print(dados_cep['logradouro'])
