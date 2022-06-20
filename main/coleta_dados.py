from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os


def coletar_dados_acao(ticker_acao):

    path_chromedriver = os.getcwd() + '/chromedriver'
    browser = webdriver.Chrome(path_chromedriver)
    url = f'https://www.google.com/search?q={ticker_acao}'
    browser.get(url)
    time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
    html = browser.page_source
    browser.close()
    soup = BeautifulSoup(html, features='html.parser')

    dados_acao = {}

    try:
        valor_abertura = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Abertura'}).get_text()
        dados_acao['capitalizacao'] = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Cap. merc.'}).get_text()
        dados_acao['dividendos'] = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Rend. div.'}).get_text()
        indice_pl = soup.find('div', {'class':'PZPZlf', 'data-attrid':'Índice P/L'}).get_text()
        fechamento = soup.find('span', {'class':'IsqQVc NprOob wT3VGc', 'jsname':'vWLAgc'}).get_text()

        dados_acao['valor_abertura'] = float(valor_abertura.replace(',', '.'))
        dados_acao['indice_pl'] = float(indice_pl.replace(',', '.'))
        dados_acao['fechamento'] = float(fechamento.replace(',', '.'))
    
    except Exception as e:
        # TODO
        # logar mensagem de erro
        return False

    return [dados_acao]


def coletar_dados_empresa(ticker_acao):

    path_chromedriver = os.getcwd() + '/chromedriver'
    browser = webdriver.Chrome(path_chromedriver)
    url = f'https://www.google.com/search?q={ticker_acao}'
    browser.get(url)
    time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
    html = browser.page_source
    browser.close()
    soup = BeautifulSoup(html, features='html.parser')

    try:
        url_dados_empresa = soup.find('a', {'class':'tiS4rf Q2MMlc'})['href']
    except Exception as e:
        # TODO logar mensagem de erro
        return False
    
    browser = webdriver.Chrome(path_chromedriver)
    browser.get(url_dados_empresa)
    time.sleep(5)  # esperar 5 segundos para carregar os dados do site.
    html = browser.page_source
    browser.close()
    soup_browser = BeautifulSoup(html, features='html.parser')
    dados_empresa = {}

    try:
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
    
    except Exception as e:
        # TODO
        # logar mensagem de erro
        return False

    return dados_empresa
