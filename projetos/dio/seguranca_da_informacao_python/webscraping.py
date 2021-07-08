from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
# objeto site recebendo o conteudo da requisição http do site
soup = BeautifulSoup(site, 'html.parser')
#objeto soup está baixando do site o html
#print(soup.prettify())
# transforma html em string e o print vai exibir o html
print(soup.title.string)
print(soup.find('admin'))