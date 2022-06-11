from coleta_acoes import coleta_dados_acao
from coleta_empresas import coleta_dados_empresa
from models import Acao, Empresa
from database.conection import open_conection_db, open_session


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

acao = Acao()
acao.empresa_id = empresa.id
acao.ticker = ticker
acao.abertura = dados_acao['valor_abertura']
acao.valor_fechamento = dados_acao['fechamento']
acao.capitalizacao = dados_acao['capitalizacao']
acao.indice_pl = dados_acao['indice_pl']
acao.rendimento_dividendos = dados_acao['dividendos']

session.add(acao)
session.commit()

conn.close()
session.close()