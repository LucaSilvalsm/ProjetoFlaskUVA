from sqlalchemy import Column, Integer, String, DECIMAL, Text
from sqlalchemy.orm import declarative_base
from .SQLCreate import engine

Base = declarative_base()

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_produto = Column(String(200), nullable=False)
    tipo_produto = Column(String(200), nullable=False)
    tamanho = Column(String(200))
    ingrediente = Column(String(200))
    preco = Column(DECIMAL(10, 2), nullable=False)
    descricao = Column(Text)
    imagem = Column(String(250), nullable=False)
    
    def __repr__(self):
        return (
            f"<Produto(id={self.id}, "
            f"nome_produto='{self.nome_produto}', "
            f"tipo_produto='{self.tipo_produto}', "
            f"tamanho='{self.tamanho}', "
            f"ingrediente='{self.ingrediente}', "
            f"preco={self.preco}, "
            f"descricao='{self.descricao}', "
            f"imagem='{self.imagem}')>"
        )

if __name__ == "__main__":
    # Associar o engine ao metadata da Base
    Base.metadata.create_all(bind=engine)
