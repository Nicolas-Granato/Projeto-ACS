from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .models import Base

urlDaDatabase = "sqlite:///clinica.db"
engine = create_engine(
    urlDaDatabase,
    connect_args={"check_same_thread": False}
)

@event.listens_for(engine, "connect")
def ativar_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

sessao = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def criarBancoDeDados():
    Base.metadata.create_all(bind=engine)

@contextmanager
def get_db():
    db = sessao()
    try:
        yield db
    finally:
        db.close() 