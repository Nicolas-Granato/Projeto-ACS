from . import models
from sqlalchemy.orm import Session
from datetime import datetime

class TutorCRUD:

    def __init__(self,db: Session):
        self.db = db

    def criar_tutor(self, nomeTutor, endereco, cidade, telefone):
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

class VeterinarioCrud:

    def __init__(self,db: Session):
        self.db = db

    def criar_veterinario(self, nomeVeterinario):
        objeto_novo_veterionario = models.Veterinario(
            nomeVeterinario=nomeVeterinario
        )

        self.db.add(objeto_novo_veterionario)
        self.db.commit()
        self.db.refresh(objeto_novo_veterionario)
    
        return objeto_novo_veterionario
    
    def lista_de_veterinarios_cadastrados(self):
        return self.db.query(models.Veterinario).all()
    
    def busca_por_veterionario_pelo_nome(self, nome_veterinario: str):
        return self.db.query(models.Veterinario).filter(models.Veterinario.nomeVeterinario.like(f"%{nome_veterinario}%")).all()

    def busca_por_veterinario_pelo_ID(self, id_veterinario: int):
        return self.db.query(models.Veterinario).filter(models.Veterinario.id == id_veterinario).first()
    
    def atualizar_veterinario(self, id_veterinario: int, nomeVeterinario_novo=None):
        veterinario = self.busca_por_veterinario_pelo_ID(id_veterinario)

        if veterinario:

            if nomeVeterinario_novo is not None:
                veterinario.nomeVeterinario = nomeVeterinario_novo
                
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

class EspecieCrud:

    def __init__(self, db: Session):
        self.db = db

    def criar_especie(self, nomeEspecie):
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

class RacaCrud:

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
    
    def delete_raca(self, id_raca: int):
        raca_para_deletar = self.busca_raca_pelo_id(id_raca)

        if raca_para_deletar:
            self.db.delete(raca_para_deletar)
            self.db.commit()
            return True
        
        return False
    
class PacienteCRUD:

    def __init__(self, db: Session):
        self.db = db
    
    def criar_paciente(self, nomePaciente, peso, porte, sexo, dataDeNascimento, raca_id, tutor_id):
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

    def atualizar_paciente(self, id_paciente, nomePaciente_novo=None, peso_novo=None, porte_novo=None, sexo_novo=None, dataDeNascimento_nova=None, raca_nova_id=None, tutor_novo_id=None):
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
    
    def deletar_paciente(self, id_paciente):
        paciente_para_deletar = self.buscar_paciente_pelo_ID(id_paciente)

        if paciente_para_deletar:
            self.db.delete(paciente_para_deletar)
            self.db.commit()

            return True
        
        return False
