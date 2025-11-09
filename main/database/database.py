from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

urlDaDatabase = "sqlite:///clinica.db"
engine = create_engine(urlDaDatabase)

sessao = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def criarBancoDeDados():
    Base.metadata.create_all(bind=engine)
