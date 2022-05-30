from sqlalchemy import create_engine
from decouple import config


def open_conection_db():
    '''Inicia uma conexão com o banco de dados e
    retorna um objeto capaz de relaizar operações no banco de dados.
    '''

    engine = create_engine(config('DATABASE_URI'))
    conn = engine.connect()

    return conn
