from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .modelos import Base, Tutor, Veterinario, Especie, Raca, Paciente, RegistroDeCondicoes, Consulta, RegistroDeCondicaoDoPaciente 

urlDaDatabase = "sqlite:///clinica.db"
engine = create_engine(urlDaDatabase)

sessao = sessionmaker(autoflush=False, autocommit=False, bind=engine)

#O resto é só abrir criar as funcoes cruds, abrindo sessao bonitinho
