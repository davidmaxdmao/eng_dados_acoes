from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.sql import func


Base = declarative_base()

class Acao(Base):
    __tablename__ = 'acao'

    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    ticker = Column(String)
    abertura = Column(Float)
    valor_fechamento = Column(Float)
    capitalizacao = Column(String)
    indice_pl = Column(Float)
    rendimento_dividendos = Column(String)
    data_ciracao = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'Ação: {self.ticker}'


class Empresa(Base):
    __tablename__ = 'empresa'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    ceo = Column(String)
    fundacao_data = Column(String)
    sede = Column(String)
    site = Column(String)

    def __repr__(self):
        return f'Empresa: {self.nome}'