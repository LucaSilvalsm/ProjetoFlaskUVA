from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import declarative_base
from .SQLCreate import engine

Base = declarative_base()

class UsuarioAdmin(Base):
    __tablename__ = "usuarioAdmin"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(30), nullable=False)
    sobrenome = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    tipo_usuario = Column(String(30), nullable=False)
    senha = Column(String(30), nullable=False)
    
    def __repr__(self):
        return f"UsuarioAdmin: \nid = {self.id}, \nnome = '{self.nome}' , \nsobrenome = '{self.sobrenome}' , \nemail = '{self.email}' , \ntipo_usuario = '{self.tipo_usuario}' , \nsenha: = '{self.senha}'"

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200), nullable=False)
    sobrenome = Column(String(200), nullable=False)
    endereco = Column(String(200), nullable=False)
    numero_casa = Column(Integer, nullable=False)
    complemento = Column(String(200), nullable=False)
    bairro = Column(String(200), nullable=False)
    telefone = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(200), nullable=False)
    tipo_usuario = Column(String(20), nullable=False) 
   
    
    def __repr__(self):
        return (
            f"<Usuario(id={self.id}, "
            f"nome='{self.nome}', "
            f"sobrenome='{self.sobrenome}', "
            f"endereco='{self.endereco}', "
            f"numero_casa={self.numero_casa}, "
            f"complemento='{self.complemento}', "
            f"bairro='{self.bairro}', "
            f"telefone='{self.telefone}', "
            f"email='{self.email}', "
            f"tipo_usuario='{self.tipo_usuario}', "
            f"senha='{self.senha}',>"
            
        )

        
if __name__ == "__main__":
    # Associar o engine ao metadata da Base
    Base.metadata.create_all(bind=engine)
