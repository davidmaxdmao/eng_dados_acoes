from coleta_acoes import coleta_dados_acao
from coleta_empresas import coleta_dados_empresa
from models import Acao, Empresa
from database.conection import open_conection_db, open_session
from gerador_csv import gerar_csv_acoes
from operacoes_sftp import OperacoesSftp

from decouple import config


def main():
    ticker = 'petr4'
    dados_acao = coleta_dados_acao(ticker)
    dados_empresa = coleta_dados_empresa(ticker)
    conn = open_conection_db()
    session = open_session()

    empresa = Empresa()
    empresa.nome = dados_empresa['acao_nome']
    empresa.ceo = dados_empresa['ceo']
    empresa.fundacao_data = dados_empresa['data_fundacao']
    empresa.sede = dados_empresa['sede']
    empresa.site = dados_empresa['site']

    session.add(empresa)
    session.commit()

    for dados in dados_acao:
        acao = Acao()
        acao.empresa_id = empresa.id
        acao.ticker = ticker
        dados['ticker'] = ticker
        acao.abertura = dados['valor_abertura']
        acao.valor_fechamento = dados['fechamento']
        acao.capitalizacao = dados['capitalizacao']
        acao.indice_pl = dados['indice_pl']
        acao.rendimento_dividendos = dados['dividendos']

        session.add(acao)
        session.commit()

        dados['data'] = acao.data_ciracao.date()
        
    arquivo = gerar_csv_acoes(dados_acao)

    if not arquivo:
        # TODO
        # Logar uma mensagem de erro
        return arquivo

    host_sftp = config('HOST_SFTP')
    port_sftp = config('PORT_SFTP', cast=int)
    user_sftp = config('USER_SFTP')
    pass_sftp = config('PASS_SFTP')
    sftp = OperacoesSftp(host_sftp, port_sftp, user_sftp, pass_sftp)
    caminho_local = f'upload/{arquivo}'
    caminho_remoto = f'/home/duki/Documentos/TI/eng-dados-estudos/projetos/ETL_acoes/main/tmp/{arquivo}'
    arquivo_enviado = sftp.enviar_arquivo(caminho_remoto, caminho_local)
    
    if not arquivo_enviado:
        # TODO
        # logar mensagem de erro
        return arquivo_enviado


    conn.close()
    session.close()

    return 'Fluxo executado com sucesso!'

main()