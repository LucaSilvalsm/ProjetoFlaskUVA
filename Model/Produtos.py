from sqlalchemy import Column, Integer, String, DECIMAL, Text
from sqlalchemy.orm import declarative_base
from .SQLCreate import engine

Base = declarative_base()

class Produto(Base):
    __tablename__ = "produtos"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome_produto = Column(String(30), nullable=False)
    tipo_produto = Column(String(30), nullable=False)
    tamanho = Column(String(50))
    ingrediente = Column(String(50))
    preco = Column(DECIMAL(10, 2), nullable=False)  # DECIMAL(10, 2) para até 10 dígitos, 2 deles após o ponto decimal
    descricao = Column(Text)
    imagem = Column(String(50), nullable=False)

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
