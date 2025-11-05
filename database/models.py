from sqlalchemy import create_engine, Column, String, Integer, Date, Text, ForeignKey, Enum, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Tutor(Base):
    __tablename__ = "tutor"

    id = Column("idTutor", Integer, primary_key=True , autoincrement=True)
    NomeTutor = Column("NomeTutor", String(255), nullable=False)
    Endereco = Column("EnderecoTutor", String(255))
    Cidade = Column("CidadeTutor", String(255))
    Telefone = Column("Telefone", String(25))

class Veterinario(Base):
    __tablename__ = "veterinario"

    id = Column("idVeterinario", Integer, primary_key=True, autoincrement=True)
    NomeVeterinario = Column("NomeVeterinario", String(255), nullable=False)

class Especie(Base):
    __tablename__ = "especie"

    id = Column("idEspecie", Integer, primary_key=True, autoincrement=True)
    NomeEspecie = Column("NomeEspecie", String(255), nullable=False)    
 
class Raca(Base):
    __tablename__ = "raca"

    id = Column("idRaca", Integer, primary_key=True, autoincrement=True)
    NomeRaca = Column("NomeRaca", String(255), nullable=False)
    Especie = Column("Especie", Integer, ForeignKey("especie.idEspecie"), nullable=False)

class Paciente(Base):
    __tablename__ = "paciente"

    id = Column("idPaciente", Integer, primary_key=True, autoincrement=True)
    NomePaciente = Column("NomePaciente", String(255), nullable=False)
    Peso = Column("Peso", Float)
    Sexo = Column(Enum("M","F", name="enum_Sexo"), nullable=False)
    DataDeNascimento = Column("DataDeNascimento", Date)
    Raca = Column("Raca", Integer, ForeignKey("raca.idRaca"))
    Tutor = Column("Tutor", Integer, ForeignKey("tutor.idTutor"))

class RegistroDeCondicoes(Base):
    __tablename__ = "registroDeCondicoes"

    id = Column("idCondicao", Integer, primary_key=True, autoincrement=True)
    NomeCondicao = Column("NomeCondicao", String(255), nullable=False)
    Descricao = Column("Descricao", Text)

class Consulta(Base):
    __tablename__ = "consulta"

    id = Column("idConsulta", Integer, primary_key=True, autoincrement=True)
    Paciente = Column("idPaciente", ForeignKey("paciente.idPaciente"))
    Veterinario = Column("idVeterinario", ForeignKey("veterinario.idVeterinario"))
    Data = Column("Data", Date, nullable=False)
    Observacoes = Column("Observacoes", Text)

class RegistroDeCondicaoDoPaciente(Base):
    __tablename__ = "registroDeCondicaoDoPaciente"

    id = Column("idRegistro", Integer, primary_key=True, autoincrement=True)
    Paciente = Column("idPaciente", Integer, ForeignKey("paciente.idPaciente"))
    Condicao = Column("idCondicao", Integer, ForeignKey("registroDeCondicoes.idCondicao"))
    Observacoes = Column("Observacoes", Text)
