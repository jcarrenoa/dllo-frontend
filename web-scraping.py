from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://es.wikipedia.org/wiki/Reino_de_Valencia"
response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for x in range(1, 4):
  h1_tags = soup.find_all(f'h{x}')
  print(f'Etiquetas h{x}: {len(h1_tags)}')