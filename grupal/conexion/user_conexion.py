from ..modelos.estudiantes import User
from .conexion import connect
from sqlmodel import SQLModel, Session, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload
import bcrypt

def autentificar_usuario(username: str, password: str) -> bool:
    engine = connect()
    with Session(engine) as sesion:
        consulta = select(User).where(User.username == username)
        resultado = sesion.exec(consulta).first()
        if resultado and validar_password(resultado.password, password):
            return True
        return False  # Validar el password

def validar_password(password_bd: str, password_ingresado: str) -> bool:
    return bcrypt.checkpw(password_ingresado.encode('utf8'), password_bd.encode('utf8'))

def crear_user(username:str,password:str,estudiante_id:int) -> bool:
    engine = connect()
    with Session(engine) as session:
        consulta = select(User).where(User.username == username)
        result = session.exec(consulta).first()
        if result:
            return "El usuario ya existe"
        
        hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        new_user = User(username=username, password=hashed_password.decode('utf-8'),estudiante_id=estudiante_id)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return "El usuario se ha creado exitosamente"
        