import csv
from datetime import datetime  


def gerar_csv_acoes(lista_dados):

    cabecalho = list(lista_dados[0].keys())
    data = datetime.today().strftime("%d-%m-%Y_%H-%M-%S")
    nome_arquivo = f'acoes_{data}.csv'

    with open(f'main/tmp/{nome_arquivo}', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=cabecalho)
        writer.writeheader()
        writer.writerows(lista_dados)

    return True

        
