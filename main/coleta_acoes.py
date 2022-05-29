from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from selenium import webdriver
import time


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = Request('https://www.google.com/search?q=petr4', headers=hdr)
html = urlopen(req)
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('div', {'class':"gyFHrc"})
print('valor da ação', nameList)#nameList.get_text())
#acao = nameList[0].get_text()[:-14]
#print(len(acao))

browser = webdriver.Chrome('../chromedriver')
url = 'https://www.google.com/search?q=petr4'
browser.get(url)
time.sleep(5)  # wait 20 seconds for the site to load.
html = browser.page_source
browser.close()

soup = BeautifulSoup(html, features='html.parser')


valor_abertura = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Abertura'}).get_text()
capitalizacao = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Cap. merc.'}).get_text()
dividendos = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Rend. div.'}).get_text()
indice_pl = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Índice P/L'}).get_text()
fechamento = soup.find('span', {'class':'IsqQVc NprOob wT3VGc', 'jsname':'vWLAgc'}).get_text()

valor_abertura_formatado = float(valor_abertura.replace(',', '.'))
valor_abertura = valor_abertura_formatado

indice_pl_formatado = float(indice_pl.replace(',', '.'))
indice_pl = indice_pl_formatado

fechamento_formatado = float(fechamento.replace(',', '.'))
fechamento = fechamento_formatado

print(valor_abertura)
print(type(valor_abertura), type(capitalizacao))
print('dividendos', dividendos, type(dividendos))
print('indice', indice_pl, type(indice_pl))
print('fechamento', fechamento, type(fechamento))
