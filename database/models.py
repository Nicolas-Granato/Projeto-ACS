from sqlalchemy import create_engine, Column, String, Integer, Date, Text, ForeignKey, Enum, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Tutor(Base):
    __tablename__ = "tabela_tutor"

    id = Column("idTutor", Integer, primary_key=True , autoincrement=True)
    nomeTutor = Column("NomeTutor", String(255), nullable=False)
    endereco = Column("EnderecoTutor", String(255))
    cidade = Column("CidadeTutor", String(255))
    telefone = Column("Telefone", String(25))

    relacaoPaciente = relationship("Paciente", back_populates="relacaoTutor")

class Veterinario(Base):
    __tablename__ = "tabela_veterinario"

    id = Column("idVeterinario", Integer, primary_key=True, autoincrement=True)
    nomeVeterinario = Column("NomeVeterinario", String(255), nullable=False)

    relacaoConsulta = relationship("Consulta", back_populates="relacaoVeterinario")

class Especie(Base):
    __tablename__ = "tabela_especie"

    id = Column("idEspecie", Integer, primary_key=True, autoincrement=True)
    nomeEspecie = Column("NomeEspecie", String(255), nullable=False)

    relacaoRaca = relationship("Raca", back_populates="relacaoEspecie")
 
class Raca(Base):
    __tablename__ = "tabela_raca"

    id = Column("idRaca", Integer, primary_key=True, autoincrement=True)
    nomeRaca = Column("NomeRaca", String(255), nullable=False)
    especie_id = Column("Especie", Integer, ForeignKey("tabela_especie.idEspecie"), nullable=False)

    relacaoEspecie = relationship("Especie", back_populates="relacaoRaca")
    relacaoPaciente_4 = relationship("Paciente", back_populates="relacaoRaca_2")

class Paciente(Base):
    __tablename__ = "tabela_paciente"

    id = Column("idPaciente", Integer, primary_key=True, autoincrement=True)
    nomePaciente = Column("NomePaciente", String(255), nullable=False)
    peso = Column("Peso", Float)
    sexo = Column(Enum("M","F", name="enum_Sexo"), nullable=False)
    dataDeNascimento = Column("DataDeNascimento", Date)
    raca_id = Column("Raca", Integer, ForeignKey("tabela_raca.idRaca"))
    tutor_id = Column("Tutor", Integer, ForeignKey("tabela_tutor.idTutor"))

    relacaoTutor = relationship("Tutor", back_populates="relacaoPaciente")
    relacaoConsulta_2 = relationship("Consulta", back_populates="relacaoPaciente_2")
    relacaoRegistroDeCondicaoDoPaciente = relationship("RegistroDeCondicaoDoPaciente", back_populates="relacaoPaciente_3")
    relacaoRaca_2 = relationship("Raca", back_populates="relacaoPaciente_4")

class RegistroDeCondicoes(Base):
    __tablename__ = "tabela_de_registros_de_condicoes"

    id = Column("idCondicao", Integer, primary_key=True, autoincrement=True)
    nomeCondicao = Column("NomeCondicao", String(255), nullable=False)
    descricao = Column("Descricao", Text)

    relacaoRegistroDeCondicaoDoPaciente_2 = relationship("RegistroDeCondicaoDoPaciente", back_populates="relacaoCondicao")

class Consulta(Base):
    __tablename__ = "tabela_consultas"

    id = Column("idConsulta", Integer, primary_key=True, autoincrement=True)
    paciente_id = Column("idPaciente", ForeignKey("tabela_paciente.idPaciente"))
    veterinario_id = Column("idVeterinario", ForeignKey("tabela_veterinario.idVeterinario"))
    data = Column("Data", Date, nullable=False)
    observacoes = Column("Observacoes", Text)

    relacaoVeterinario = relationship("Veterinario", back_populates="relacaoConsulta")
    relacaoPaciente_2 = relationship("Paciente", back_populates="relacaoConsulta_2")

class RegistroDeCondicaoDoPaciente(Base):
    __tablename__ = "tabela_de_registro_de_condicao_do_paciente"

    id = Column("idRegistro", Integer, primary_key=True, autoincrement=True)
    paciente_id = Column("idPaciente", Integer, ForeignKey("tabela_paciente.idPaciente"))
    condicao_id = Column("idCondicao", Integer, ForeignKey("tabela_de_registros_de_condicoes.idCondicao"))
    observacoes = Column("Observacoes", Text)

    relacaoPaciente_3 = relationship("Paciente", back_populates="relacaoRegistroDeCondicaoDoPaciente")
    relacaoCondicao = relationship("RegistroDeCondicoes", back_populates="relacaoRegistroDeCondicaoDoPaciente_2")
