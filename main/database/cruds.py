from . import models
from sqlalchemy.orm import Session
from datetime import datetime

class TutorCRUD:

    def __init__(self,db: Session):
        self.db = db

    