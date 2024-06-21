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
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(30), nullable=False)
    sobrenome = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    senha = Column(String(30), nullable=False)
    telefone = Column(String(30), nullable=False, unique=True)
    endereco = Column(String(50), nullable=False)
    tipo_usuario = Column(String(50), nullable=False)
    numero_casa = Column(String(10), nullable=False)
    complemento = Column(String(50), nullable=False)
    bairro = Column(String(30), nullable=False)
    
    def __repr__(self):
        return f"Usuario: \nId = {self.id}, \nTipo_usuario = '{self.tipo_usuario}',\nNome = '{self.nome}' , \nSobrenome = '{self.sobrenome}' , \nEmail = '{self.email}' , \nTelefone = '{self.telefone}' , \nSenha: = '{self.senha}' , \nEndereço = '{self.endereco}' , \nNumero da Casa = '{self.numero_casa}' , \nComplemento = '{self.complemento}' , \nBairro = '{self.bairro}'"

   
        
if __name__ == "__main__":
    # Associar o engine ao metadata da Base
    Base.metadata.create_all(bind=engine)
