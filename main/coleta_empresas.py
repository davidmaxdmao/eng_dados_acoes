from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import os


path_chromedriver = os.getcwd() + '/chromedriver'
browser = webdriver.Chrome(path_chromedriver)
url = 'https://www.google.com/finance/quote/PETR4:BVMF?sa=X&ved=2ahUKEwi6' \
    '5caWqvn3AhUtkpUCHeC7C-MQ3ecFegQIAxAi'

browser.get(url)
time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
html = browser.page_source
browser.close()
soup_browser = BeautifulSoup(html, features='html.parser')
ceo = soup_browser.find(
    'a',
    {
        'class': 'tBHE4e',
        'target': '_blank',
        'href': 'https://www.google.com/search?q=Jos%C3%A9%20Mauro%20Ferreira%20Coelho&hl=pt-BR'
    }
).get_text()

html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
acao_nome = soup.find('div', {'role':'heading', 'class':'zzDege', }).get_text()
data_fundacao = soup.findAll('div', {'class':'P6K39c'})[9].get_text()
sede = soup.findAll(
    'a',
    {
        'target': '_blank',
        'class': 'tBHE4e',
    }
)[1].get_text()

site = soup.findAll(
    'a',
    {
        'target': '_blank',
        'class': 'tBHE4e',
    }
)[2].get_text()


print(acao_nome)
print(ceo)
print(data_fundacao)
print(sede)
print(site)