from sqlalchemy import Column, ForeignKey, Enum, String, Integer, Date, Text, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Tutor(Base):
    __tablename__ = "tabela_tutor"

    id = Column("idTutor", Integer, primary_key=True , autoincrement=True)
    nomeTutor = Column("NomeTutor", String(255), nullable=False)
    endereco = Column("EnderecoTutor", String(255))
    cidade = Column("CidadeTutor", String(255))
    telefone = Column("Telefone", String(25))

    pacientes = relationship("Paciente", back_populates="tutor")

class Veterinario(Base):
    __tablename__ = "tabela_veterinario"

    id = Column("idVeterinario", Integer, primary_key=True, autoincrement=True)
    nomeVeterinario = Column("NomeVeterinario", String(255), nullable=False)
    nivelDeAcesso = Column(Enum("Administrador","Usuário", name="enum_NivelDeAcesso"), nullable=False)
    hashSenha = Column("HashSenha", String(255), nullable=False)

    consultas = relationship("Consulta", back_populates="veterinario")

class Especie(Base):
    __tablename__ = "tabela_especie"

    id = Column("idEspecie", Integer, primary_key=True, autoincrement=True)
    nomeEspecie = Column("NomeEspecie", String(255), nullable=False)

    racas = relationship("Raca", back_populates="especie")
    
class Raca(Base):
    __tablename__ = "tabela_raca"

    id = Column("idRaca", Integer, primary_key=True, autoincrement=True)
    nomeRaca = Column("NomeRaca", String(255), nullable=False)
    especie_id = Column("Especie", Integer, ForeignKey("tabela_especie.idEspecie"), nullable=False)

    especie = relationship("Especie", back_populates="racas")
    pacientes = relationship("Paciente", back_populates="raca")

class Paciente(Base):
    __tablename__ = "tabela_paciente"

    id = Column("idPaciente", Integer, primary_key=True, autoincrement=True)
    nomePaciente = Column("NomePaciente", String(255), nullable=False)
    peso = Column("Peso", Float)
    porte = Column(Enum("Gigante","Grande","Medio","Pequeno", name="enum_Porte"), nullable=False)
    sexo = Column(Enum("M","F", name="enum_Sexo"), nullable=False)
    dataDeNascimento = Column("DataDeNascimento", Date)
    raca_id = Column("Raca", Integer, ForeignKey("tabela_raca.idRaca"))
    tutor_id = Column("Tutor", Integer, ForeignKey("tabela_tutor.idTutor"))

    tutor = relationship("Tutor", back_populates="pacientes")
    consultas = relationship("Consulta", back_populates="paciente")
    registros_condicao = relationship("RegistroDeCondicaoDoPaciente", back_populates="paciente")
    raca = relationship("Raca", back_populates="pacientes")

class RegistroDeCondicoes(Base):
    __tablename__ = "tabela_de_registros_de_condicoes"

    id = Column("idCondicao", Integer, primary_key=True, autoincrement=True)
    nomeCondicao = Column("NomeCondicao", String(255), nullable=False)
    descricao = Column("Descricao", Text)

    registros_paciente = relationship("RegistroDeCondicaoDoPaciente", back_populates="condicao")

class Consulta(Base):
    __tablename__ = "tabela_consultas"

    id = Column("idConsulta", Integer, primary_key=True, autoincrement=True)
    paciente_id = Column("idPaciente", ForeignKey("tabela_paciente.idPaciente"))
    veterinario_id = Column("idVeterinario", ForeignKey("tabela_veterinario.idVeterinario"))
    data = Column("Data", Date, nullable=False)
    observacoes = Column("Observacoes", Text)

    veterinario = relationship("Veterinario", back_populates="consultas")
    paciente = relationship("Paciente", back_populates="consultas")

class RegistroDeCondicaoDoPaciente(Base):
    __tablename__ = "tabela_de_registro_de_condicao_do_paciente"

    id = Column("idRegistro", Integer, primary_key=True, autoincrement=True)
    paciente_id = Column("idPaciente", Integer, ForeignKey("tabela_paciente.idPaciente"))
    condicao_id = Column("idCondicao", Integer, ForeignKey("tabela_de_registros_de_condicoes.idCondicao"))
    observacoes = Column("Observacoes", Text)

    paciente = relationship("Paciente", back_populates="registros_condicao")
    condicao = relationship("RegistroDeCondicoes", back_populates="registros_paciente")
