from database.cruds import UsuarioCRUD
from sqlalchemy.orm import Session
import bcrypt

class Autenticacao:
    def __init__(self, db: Session):
        self.crud = UsuarioCRUD(db)
    
    def login(self, username: str, senha_plana: str):
        usuario = self.crud.busca_usuario_pelo_username(username)
        
        if not usuario:
            print(f"Usuario {username} não encontrado.")
            return None
        
        try:
            senha_plana_bytes = senha_plana.encode("utf-8")
            hash_armazenado_bytes = usuario.senha_hash.encode("utf-8")

            if bcrypt.checkpw(senha_plana_bytes, hash_armazenado_bytes):
                return usuario

            return None
        
        except ValueError:
            return None
    
#    def redefinirSenha(self, username: str, senha_plana: str):  
