# dao/UsuarioDAO.py
from Model.UsuarioSQL import Usuario
from Model.SQLCreate import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class UsuarioDAO:
    
    def incluir(self, usuario):
        session.add(usuario)
        session.commit()

    def obter(self, id):
        return session.query(Usuario).filter_by(id=id).first()
    def obter_por_email(self, email):
        # Lógica para buscar um usuário pelo email no banco de dados
        # Exemplo hipotético:
        usuario = session.query(Usuario).filter_by(email=email).first()
        return usuario if usuario else None
    def obter_por_telefone(self, telefone):
        usuario = session.query(Usuario).filter_by(telefone=telefone).first()
        return usuario if usuario else None

