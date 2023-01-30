import requests
from bs4 import BeautifulSoup 

usuario_github = input('Insira o usuario do github: ')
url = 'https://github.com/'+usuario_github
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')
imagem_perfil = soup.find('img', {'alt' : 'Avatar'})['src']
print(imagem_perfil)
