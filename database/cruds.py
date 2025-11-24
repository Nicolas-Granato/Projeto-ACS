from . import models
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import date
import bcrypt

class TutorCRUD:

    def __init__(self,db: Session):
        self.db = db

    def criar_tutor(self, nomeTutor: str, endereco: str, cidade: str, telefone: str):
        objeto_novo_tutor = models.Tutor(
            nomeTutor=nomeTutor,
            endereco=endereco,
            cidade=cidade,
            telefone=telefone
        )

        self.db.add(objeto_novo_tutor)
        self.db.commit()
        self.db.refresh(objeto_novo_tutor)

        return objeto_novo_tutor
    
    def lista_de_tutores_cadastrados(self):
        return self.db.query(models.Tutor).all()
    
    def busca_por_tutor_pelo_nome(self, nome_tutor: str):
        return self.db.query(models.Tutor).filter(models.Tutor.nomeTutor.like(f"%{nome_tutor}%")).all()
    
    def busca_por_tutor_pelo_ID(self, tutor_id: int):
        return self.db.query(models.Tutor).filter(models.Tutor.id == tutor_id).first()

    def atualizar_tutor(self, tutor_id: int, nomeTutor_novo=None, endereco_novo=None, cidade_nova=None, telefone_novo=None):
        tutor = self.busca_por_tutor_pelo_ID(tutor_id)

        if tutor:
            if nomeTutor_novo is not None:
                tutor.nomeTutor = nomeTutor_novo
            if endereco_novo is not None:
                tutor.endereco = endereco_novo
            if cidade_nova is not None:
                tutor.cidade = cidade_nova
            if telefone_novo is not None:
                tutor.telefone = telefone_novo
            
            self.db.commit()
            self.db.refresh(tutor)
            return tutor

        return None
    
    def deletar_tutor(self, tutor_id: int):
        tutor_para_deletar = self.busca_por_tutor_pelo_ID(tutor_id)

        if tutor_para_deletar:
            self.db.delete(tutor_para_deletar)
            self.db.commit()

            return True

        return False

class VeterinarioCRUD:

    def __init__(self,db: Session):
        self.db = db

    def criar_veterinario(self, idDeusuario: int, nomeVeterinario: str, CRM: str):
        objeto_novo_veterionario = models.Veterinario(
            idDeusuario=idDeusuario,
            CRM=CRM
        )

        self.db.add(objeto_novo_veterionario)
        self.db.commit()
        self.db.refresh(objeto_novo_veterionario)
    
        return objeto_novo_veterionario
    
    def lista_de_veterinarios_cadastrados(self):
        return self.db.query(models.Veterinario).all()
    
    def busca_por_veterinario_pelo_nome(self, nome_veterinario: str):
        return self.db.query(models.Veterinario).join(models.Usuario).filter(models.Usuario.nome.like(f"%{nome_veterinario}%")).all()

    def busca_por_veterinario_pelo_ID(self, id_veterinario: int):
        return self.db.query(models.Veterinario).filter(models.Veterinario.id == id_veterinario).first()
    
    def atualizar_veterinario(self, id_veterinario: int, CRM_novo=None):
        veterinario = self.busca_por_veterinario_pelo_ID(id_veterinario)

        if veterinario:

            if CRM_novo is not None:
                veterinario.CRM = CRM_novo
                
            self.db.commit()
            self.db.refresh(veterinario)

            return veterinario
        
        return None

        
    def deletar_veterinario(self, id_veterinario: int):
        veterinario_para_deletar = self.busca_por_veterinario_pelo_ID(id_veterinario)

        if veterinario_para_deletar:
            self.db.delete(veterinario_para_deletar)
            self.db.commit()
            
            return True

        return False

class EspecieCRUD:

    def __init__(self, db: Session):
        self.db = db

    def criar_especie(self, nomeEspecie: str):
        objeto_nova_especie = models.Especie(
            nomeEspecie = nomeEspecie
        )

        self.db.add(objeto_nova_especie)
        self.db.commit()
        self.db.refresh(objeto_nova_especie)

    def lista_de_especies_cadastradas(self):
        return self.db.query(models.Especie).all()
    
    def buscar_especie_pelo_ID(self, id_especie: int):
        return self.db.query(models.Especie).filter(models.Especie.id == id_especie).first()
    
    def buscar_especie_pelo_nome(self, nome_especie: str):
        return self.db.query(models.Especie).filter(models.Especie.nomeEspecie.like(f"%{nome_especie}%")).all()
    
    def atualizar_especie(self, id_especie: int, nomeEspecie_novo=None):
        especie = self.buscar_especie_pelo_ID(id_especie)

        if especie:
            if nomeEspecie_novo is not None:
                especie.nomeEspecie = nomeEspecie_novo

            self.db.commit()
            self.db.refresh(especie)
            return especie
            
        return None
    
    def deletar_especie(self, id_especie: int):
        especie_para_deletar = self.buscar_especie_pelo_ID(id_especie)

        if especie_para_deletar:
            self.db.delete(especie_para_deletar)
            self.db.commit()

            return True
        
        return False

class RacaCRUD:

    def __init__(self, db: Session):
        self.db = db
    
    def criar_raca(self, nomeRaca: str, especie_id: int):
        obj_raca = models.Raca(
            nomeRaca=nomeRaca,
            especie_id=especie_id
        )
        self.db.add(obj_raca)
        self.db.commit()
        self.db.refresh(obj_raca)

        return obj_raca
    
    def lista_de_racas_cadastradas(self):
        return self.db.query(models.Raca).all()
    
    def busca_raca_pelo_id(self, id_raca: int):
        return self.db.query(models.Raca).filter(models.Raca.id == id_raca).first()
    
    def busca_raca_pelo_nome(self, nomeRaca: str):
        return self.db.query(models.Raca).filter(models.Raca.nomeRaca.like(f"%{nomeRaca}%")).all()
    
    def atualizar_raca(self, id_raca: int, nomeRaca_novo=None, especie_nova_id=None):
        raca_para_atualizar = self.busca_raca_pelo_id(id_raca)

        if raca_para_atualizar:
            if nomeRaca_novo is not None:
                raca_para_atualizar.nomeRaca = nomeRaca_novo
            if especie_nova_id is not None:
                raca_para_atualizar.especie_id = especie_nova_id

            self.db.commit()
            self.db.refresh(raca_para_atualizar)
            return raca_para_atualizar
        
        return None
    
    def deletar_raca(self, id_raca: int):
        raca_para_deletar = self.busca_raca_pelo_id(id_raca)

        if raca_para_deletar:
            self.db.delete(raca_para_deletar)
            self.db.commit()
            return True
        
        return False
    
class PacienteCRUD:

    def __init__(self, db: Session):
        self.db = db
    
    def criar_paciente(self, nomePaciente: str, peso: int, porte: int, sexo: str, dataDeNascimento: date, raca_id: int, tutor_id: int):
        obj_paciente = models.Paciente(
            nomePaciente=nomePaciente,
            peso=peso,
            porte=porte,
            sexo=sexo,
            dataDeNascimento=dataDeNascimento,
            raca_id=raca_id,
            tutor_id=tutor_id
        )
        self.db.add(obj_paciente)
        self.db.commit()
        self.db.refresh(obj_paciente)

        return obj_paciente
    
    def lista_de_pacientes_cadastrados(self):
        return self.db.query(models.Paciente).all()
    
    def buscar_paciente_pelo_ID(self, id_paciente: int):
        return self.db.query(models.Paciente).filter(models.Paciente.id == id_paciente).first()
    
    def busca_paciente_pelo_nome(self, nomePaciente: str):
        return self.db.query(models.Paciente).filter(models.Paciente.nomePaciente.like(f"%{nomePaciente}%")).all()
    
    def busca_pacientes_pelo_tutor(self, id_tutor: int):
        return self.db.query(models.Paciente).filter(models.Paciente.tutor_id == id_tutor).all()
    
    def busca_pacientes_pela_raca(self, id_raca: int):
        return self.db.query(models.Paciente).filter(models.Paciente.raca_id == id_raca).all()

    def atualizar_paciente(self, id_paciente: int, nomePaciente_novo=None, peso_novo=None, porte_novo=None, sexo_novo=None, dataDeNascimento_nova=None, raca_nova_id=None, tutor_novo_id=None):
        paciente_para_atualizar = self.buscar_paciente_pelo_ID(id_paciente)
        
        if paciente_para_atualizar:
            if nomePaciente_novo is not None:
                paciente_para_atualizar.nomePaciente = nomePaciente_novo
            if peso_novo is not None:
                paciente_para_atualizar.peso = peso_novo
            if porte_novo is not None:
                paciente_para_atualizar.porte = porte_novo
            if sexo_novo is not None:
                paciente_para_atualizar.sexo = sexo_novo
            if dataDeNascimento_nova is not None:
                paciente_para_atualizar.dataDeNascimento = dataDeNascimento_nova
            if raca_nova_id is not None:
                paciente_para_atualizar.raca_id = raca_nova_id
            if tutor_novo_id is not None:
                paciente_para_atualizar.tutor_id = tutor_novo_id
            
            self.db.commit()
            self.db.refresh(paciente_para_atualizar)

            return paciente_para_atualizar
    
        return None
    
    def deletar_paciente(self, id_paciente: int):
        paciente_para_deletar = self.buscar_paciente_pelo_ID(id_paciente)

        if paciente_para_deletar:
            self.db.delete(paciente_para_deletar)
            self.db.commit()

            return True
        
        return False

class RegistroDeCondicoesCRUD:

    def __init__(self, db: Session):
        self.db = db

    def criar_registro_de_condicao(self, nomeCondicao: str, descricao: str):
        obj_registro = models.RegistroDeCondicoes(
            nomeCondicao=nomeCondicao,
            descricao=descricao
        )
        
        self.db.add(obj_registro)
        self.db.commit()
        self.db.refresh(obj_registro)

        return obj_registro
    
    def lista_de_condicoes(self):
        return self.db.query(models.RegistroDeCondicoes).all()
    
    def busca_condicao_pelo_ID(self, id_condicao: int):
        return self.db.query(models.RegistroDeCondicoes).filter(models.RegistroDeCondicoes.id == id_condicao).first()
    
    def busca_condicao_pelo_nome(self, nome_condicao: str):
        return self.db.query(models.RegistroDeCondicoes).filter(models.RegistroDeCondicoes.nomeCondicao.like(f"%{nome_condicao}%")).all()
    
    def atualizar_condicao(self, id_condicao: int, nome_novo_condicao=None, descricao_nova=None):
        condicao_para_atualizar = self.busca_condicao_pelo_ID(id_condicao)
        if condicao_para_atualizar:
            if nome_novo_condicao is not None:
                condicao_para_atualizar.nomeCondicao = nome_novo_condicao
            if descricao_nova is not None:
                condicao_para_atualizar.descricao = descricao_nova
            
            self.db.commit()
            self.db.refresh(condicao_para_atualizar)
            
            return condicao_para_atualizar
        
        return None
    
    def deletar_condicao(self, id_condicao: int):
        condicao_para_deletar = self.busca_condicao_pelo_ID(id_condicao)

        if condicao_para_deletar:

            self.db.delete(condicao_para_deletar)
            self.db.commit()
        
            return True
        
        return False
    
class ConsultasCRUD:

    def __init__(self, db: Session):
        self.db = db

    def criar_consulta(self, paciente_id: int, veterinario_id: int, data: date, observacoes: str):
        obj_consulta = models.Consulta(
            paciente_id=paciente_id,
            veterinario_id=veterinario_id,
            data=data,
            observacoes=observacoes
        )

        self.db.add(obj_consulta)
        self.db.commit()
        self.db.refresh(obj_consulta)

        return obj_consulta
    
    def lista_consultas(self):
        return self.db.query(models.Consulta).all()
    
    def busca_consulta_pelo_ID(self, id_consulta: int):
        return self.db.query(models.Consulta).filter(models.Consulta.id == id_consulta).first()
    
    def busca_consulta_pelo_paciente(self, id_paciente: int):
        return self.db.query(models.Consulta).filter(models.Consulta.paciente_id == id_paciente).all()
    
    def busca_consulta_pelo_veterinario(self, id_veterinario: int):
        return self.db.query(models.Consulta).filter(models.Consulta.veterinario_id == id_veterinario).all()
    
    def busca_consulta_pela_data(self, data: date):
        return self.db.query(models.Consulta).filter(models.Consulta.data == data).all()
    
    def atualizar_consulta(self, id_consulta: int, paciente_id_novo=None, veterinario_id_novo=None, data_nova=None, observacoes_novas=None):
        consulta_para_atualizar = self.busca_consulta_pelo_ID(id_consulta)

        if consulta_para_atualizar:
            if paciente_id_novo is not None:
                consulta_para_atualizar.paciente_id = paciente_id_novo
            if veterinario_id_novo is not None:
                consulta_para_atualizar.veterinario_id = veterinario_id_novo
            if data_nova is not None:
                consulta_para_atualizar.data = data_nova
            if observacoes_novas is not None:
                consulta_para_atualizar.observacoes = observacoes_novas
            
            self.db.commit()
            self.db.refresh(consulta_para_atualizar)

            return consulta_para_atualizar
        
        return None
    
    def deletar_consulta(self, id_consulta: int):
        consulta_para_deletar = self.busca_consulta_pelo_ID(id_consulta)

        if consulta_para_deletar:
            self.db.delete(consulta_para_deletar)
            self.db.commit()

            return True
        
        return False
    
class RegistroDeCondicaoDoPacienteCRUD:

    def __init__(self, db: Session):
        self.db = db
        
    def criar_registro_de_condicao_do_paciente(self, paciente_id: int, condicao_id: int, observacoes: str):
        obj_registro_de_condicao = models.RegistroDeCondicaoDoPaciente(
            paciente_id=paciente_id,
            condicao_id=condicao_id,
            observacoes=observacoes
        )
        
        self.db.add(obj_registro_de_condicao)
        self.db.commit()
        self.db.refresh(obj_registro_de_condicao)

        return obj_registro_de_condicao

    def lista_registros_de_condicao_do_paciente(self):
        return self.db.query(models.RegistroDeCondicaoDoPaciente).all()
    
    def busca_registro_de_condicao_do_paciente_pelo_ID(self, id_registro_de_condicao: int):
        return self.db.query(models.RegistroDeCondicaoDoPaciente).filter(models.RegistroDeCondicaoDoPaciente.id == id_registro_de_condicao).first()
    
    def busca_registro_de_condicao_do_paciente_pelo_paciente(self, id_paciente: int):
        return self.db.query(models.RegistroDeCondicaoDoPaciente).filter(models.RegistroDeCondicaoDoPaciente.paciente_id == id_paciente).all()
    
    def busca_registro_de_condicao_do_paciente_pela_condicao(self, id_condicao: int):
        return self.db.query(models.RegistroDeCondicaoDoPaciente).filter(models.RegistroDeCondicaoDoPaciente.condicao_id == id_condicao).all()
    
    def atualizar_registro_de_condicao_do_paciente(self, id_registro_de_condicao: int, paciente_id_novo=None, condicao_id_nova=None, observacoes_novas=None):
        registro_para_atualizar = self.busca_registro_de_condicao_do_paciente_pelo_ID(id_registro_de_condicao)
        
        if registro_para_atualizar:
            if paciente_id_novo is not None:
                registro_para_atualizar.paciente_id = paciente_id_novo
            if condicao_id_nova is not None:
                registro_para_atualizar.condicao_id = condicao_id_nova
            if observacoes_novas is not None:
                registro_para_atualizar.observacoes = observacoes_novas
            
            self.db.commit()
            self.db.refresh(registro_para_atualizar)

            return registro_para_atualizar
        
        return None
    
    def deletar_registro_de_condicao_do_paciente(self, id_registro: int):
        registro_para_deletar = self.busca_registro_de_condicao_do_paciente_pelo_ID(id_registro)

        if registro_para_deletar:
            self.db.delete(registro_para_deletar)
            self.db.commit()

            return True
        
        return False

class UsuarioCRUD:
    def __init__(self, db: Session):
        self.db = db
    
    def criar_usuario(self, nome: str, username: str, senha_plana: str, nivelDeAcesso: str):
        salt = bcrypt.gensalt()
        senha_hashed = bcrypt.hashpw(senha_plana.encode("utf-8"), salt)

        obj_usuario = models.Usuario(
            nome=nome,
            username=username,
            senha_hash=senha_hashed.decode("utf-8"),
            nivelDeAcesso=nivelDeAcesso
        )

        try:
            self.db.add(obj_usuario)
            self.db.commit()
            self.db.refresh(obj_usuario)

            return obj_usuario
        
        except IntegrityError as e:
            print(f"Erro: O nome de usuário '{username}' já existe. Detalhes: {e}")
            self.db.rollback()
            
            return None
        
    def busca_usuario_pelo_ID(self, id_usuario: int):
        return self.db.query(models.Usuario).filter(models.Usuario.id == id_usuario).first()
        
    def atualizar_usuario(self, id_usuario: int, nome_novo=None, username_novo=None, senha_nova=None):

        usuario_para_atualizar = self.busca_usuario_pelo_ID(id_usuario)

        if usuario_para_atualizar:
            if nome_novo is not None:
                usuario_para_atualizar.nome = nome_novo
            if username_novo is not None:
                usuario_para_atualizar.username = username_novo
            if senha_nova is not None:
                salt = bcrypt.gensalt()
                senha_hashed = bcrypt.hashpw(senha_nova.encode("utf-8"), salt)
                usuario_para_atualizar.senha_hash = senha_hashed.decode("utf-8")
        
            self.db.commit()
            self.db.refresh(usuario_para_atualizar)
            return usuario_para_atualizar
        
        return None
    
    def deletar_usuario(self, id_usuario: int):
        usuario_para_deletar = self.busca_usuario_pelo_ID(id_usuario)

        if usuario_para_deletar:
            self.db.delete(usuario_para_deletar)
            self.db.commit()

            return True
        
        return False
