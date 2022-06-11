from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import os


def coleta_dados_empresa(ticker_acao):

    path_chromedriver = os.getcwd() + '/chromedriver'
    browser = webdriver.Chrome(path_chromedriver)
    url = f'https://www.google.com/search?q={ticker_acao}'
    browser.get(url)
    time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
    html = browser.page_source
    browser.close()
    soup = BeautifulSoup(html, features='html.parser')
    url_dados_empresa = soup.find('a', {'class':'tiS4rf Q2MMlc'})['href']
    
    browser = webdriver.Chrome(path_chromedriver)
    browser.get(url_dados_empresa)
    time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
    html = browser.page_source
    browser.close()
    soup_browser = BeautifulSoup(html, features='html.parser')
    dados_empresa = {}
    dados_empresa['ceo'] = soup_browser.find(
        'a',
        {
            'class': 'tBHE4e',
            'target': '_blank',
            'href': 'https://www.google.com/search?q=Jos%C3%A9%20Mauro%20Ferreira%20Coelho&hl=pt-BR'
        }
    ).get_text()

    dados_empresa['acao_nome'] = soup_browser.find('div', {'role':'heading', 'class':'zzDege', }).get_text()
    dados_empresa['data_fundacao'] = soup_browser.findAll('div', {'class':'P6K39c'})[10].get_text()
    dados_empresa['sede'] = soup_browser.find(
        'a',
        {
            'target': '_blank',
            'class': 'tBHE4e',
            'href': 'https://www.google.com/maps/place/Av.%20Republica%20do%20Chile%2C%20Rio%20de%20Janeiro%2C%20Rio'\
                '%20de%20Janeiro%2C%20Brasil?hl=pt-BR'
        }
    ).get_text()

    dados_empresa['site'] = soup_browser.find(
        'a',
        {
            'target': '_blank',
            'class': 'tBHE4e',
            'href': 'http://petrobras.com.br/'
        }
    ).get_text()

    return dados_empresa
