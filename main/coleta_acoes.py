from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os


path_chromedriver = os.getcwd() + '/chromedriver'
browser = webdriver.Chrome(path_chromedriver)
url = 'https://www.google.com/search?q=petr4'
browser.get(url)
time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
html = browser.page_source
browser.close()
soup = BeautifulSoup(html, features='html.parser')

valor_abertura = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Abertura'}).get_text()
capitalizacao = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Cap. merc.'}).get_text()
dividendos = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Rend. div.'}).get_text()
indice_pl = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Índice P/L'}).get_text()
fechamento = soup.find('span', {'class':'IsqQVc NprOob wT3VGc', 'jsname':'vWLAgc'}).get_text()

valor_abertura = float(valor_abertura.replace(',', '.'))
indice_pl = float(indice_pl.replace(',', '.'))
fechamento = float(fechamento.replace(',', '.'))


print(valor_abertura)
print(type(valor_abertura), type(capitalizacao))
print('dividendos', dividendos, type(dividendos))
print('indice', indice_pl, type(indice_pl))
print('fechamento', fechamento, type(fechamento))
