from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os


def coleta_dados_acao(ticker_acao):

    path_chromedriver = os.getcwd() + '/chromedriver'
    browser = webdriver.Chrome(path_chromedriver)
    url = f'https://www.google.com/search?q={ticker_acao}'
    browser.get(url)
    time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
    html = browser.page_source
    browser.close()
    soup = BeautifulSoup(html, features='html.parser')

    dados_acao = {}
    valor_abertura = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Abertura'}).get_text()
    dados_acao['capitalizacao'] = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Cap. merc.'}).get_text()
    dados_acao['dividendos'] = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Rend. div.'}).get_text()
    indice_pl = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Índice P/L'}).get_text()
    fechamento = soup.find('span', {'class':'IsqQVc NprOob wT3VGc', 'jsname':'vWLAgc'}).get_text()

    dados_acao['valor_abertura'] = float(valor_abertura.replace(',', '.'))
    dados_acao['indice_pl'] = float(indice_pl.replace(',', '.'))
    dados_acao['fechamento'] = float(fechamento.replace(',', '.'))

    return [dados_acao]
