from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

urlDaDatabase = "sqlite:///clinica.db"
engine = create_engine(
    urlDaDatabase,
    connect_args={"check_same_thread": False}   
)

sessao = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def criarBancoDeDados():
    Base.metadata.create_all(bind=engine)

def get_db():

    db = sessao()

    try:

        yield db
    finally:
        db.close()
