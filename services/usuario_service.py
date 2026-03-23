from database.cruds import UsuarioCRUD
from sqlalchemy.orm import Session
import bcrypt

    def login(self, username: str, senha_plana: str):
            usuario = self.crud.busca_usuario_pelo_username(username)
             
            if not usuario:
                return None
            
            try:
                senha_plana_bytes = senha_plana.encode("utf-8")
                hash_armazenado_bytes = usuario.senha_hash.encode("utf-8")

                if bcrypt.checkpw(senha_plana_bytes, hash_armazenado_bytes):

                    return usuario

                return None
            
            except ValueError:
                return None
        
    def redefinirSenha(self, username: str, senha_plana: str):  
        usuario = self.crud.busca_usuario_pelo_username(username)
        
        if not usuario:
            return None
            
        try:
            senha_plana_bytes = senha_plana.encode("utf-8")
            hash_novo_bytes = bcrypt.hashpw(senha_plana_bytes, bcrypt.gensalt())
            hash_novo_str = hash_novo_bytes.decode("utf-8")
        
            usuario.senha_hash = hash_novo_str
            self.crud.atualiza_usuario(usuario)

            return usuario
            
        except ValueError:
            return None
