from database.cruds import UsuarioCRUD
from sqlalchemy.orm import Session
import smtplib
from email.message import EmailMessage
import ssl
import random

class Autenticacao:
    def __init__(self, db: Session):
        self.crud = UsuarioCRUD(db)

    def gerar_codigo_de_verificacao():
        token = random.randint(100000, 999999)
        return token
    
    def enviar_codigo_por_email(self, email_de_destino: str, to: str, username: str, token: int,):
        SMTP_host = "smtp.gmail.com"
        SMTP_port = 587

        msg = EmailMessage()
        msg["Subject"] = "Código de Verificação"
        msg["From"] = "nicolas.barbosajf@gmail.com"
        msg["To"] = email_de_destino
        msg.set_content(f"Olá {username},\n\nSeu código de verificação é: {token}\n\nSe você não solicitou este código, por favor ignore este email.\n\nAtenciosamente,\nEquipe de Suporte")