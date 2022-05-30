from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config


def open_conection_db():
    '''Inicia uma conexão com o banco de dados e
    retorna um objeto capaz de relaizar operações no banco de dados.
    '''

    engine = create_engine(config('DATABASE_URI'))
    conn = engine.connect()

    return conn

def open_session():

    engine = open_conection_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    return session
