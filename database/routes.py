from . import models
from sqlalchemy.orm import Session
from datetime import datetime

class TutorCRUD:

    def __init__(self,db: Session):
        self.db = db

    def criar_tutor(self, nomeTutor, endereco, cidade, telefone):
        objetoNovoTutor = models.Tutor(
            nomeTutor=nomeTutor,
            endereco=endereco,
            cidade=cidade,
            telefone=telefone
        )

        self.db.add(objetoNovoTutor)
        self.db.commit()
        self.db.refresh(objetoNovoTutor)

        return objetoNovoTutor
    
    def lista_de_tutores_cadastrados(self):
        return self.db.query(models.Tutor).all()
    
    def busca_por_tutor_pelo_nome(self, nome_tutor: str):
        return self.db.query(models.Tutor).filter(models.Tutor.nomeTutor.like(f"%{nome_tutor}%")).all()
    
    def busca_por_tutor_pelo_ID(self, tutor_id: int):
        return self.db.query(models.Tutor).filter(models.Tutor.id == tutor_id).first()

    def atualizar_tutor(self, nome_novo: str):
        return
    
    def deletar_tutor(self, tutor_id: int):
        tutor_para_deletar = self.busca_por_tutor_pelo_ID(tutor_id)

        if tutor_para_deletar:
            self.db.delete(tutor_para_deletar)
            self.db.commit()

class VeterinarioCrud:

    def __init__(self,db: Session):
        self.db = db

    