from sqlalchemy import Column,Integer,String,ForeignKey,DECIMAL,Text,TIMESTAMP
from sqlalchemy.orm import declarative_base,relationship
from .SQLCreate import engine
from sqlalchemy.sql import func  


Base = declarative_base ()

class Carrinho(Base):
    __tablename__ = "carrinho"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    nome_produto = Column(String(50), nullable=False)
    imagem_produto = Column(String(50), nullable=False)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)  # Renomeado para 'produtos.id'
    quantidade = Column(Integer, nullable=False)
    observacao = Column(Text)
    preco_total = Column(DECIMAL(10, 2), nullable=False)
    
    usuario_id = relationship("Usuario")
    produto_id = relationship("Produto")  # Renomeado para 'Produto' para seguir a convenção de classe
    
    def __repr__(self):
        return (
            f"<Carrinho(id={self.id}, "
            f"usuario_id={self.usuario_id}, "
            f"nome_produto='{self.nome_produto}', "
            f"imagem_produto='{self.imagem_produto}', "
            f"produto_id={self.produto_id}, "
            f"quantidade={self.quantidade}, "
            f"observacao='{self.observacao}', "
            f"preco_total={self.preco_total})>"
        )



class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    data_pedido = Column(TIMESTAMP, default=func.now(), nullable=False)  # Use default=func.now() aqui
    forma_pagamento = Column(String(30), nullable=False)
    endereco_entrega = Column(String(50))
    status = Column(String(30), nullable=False)
    valor_total = Column(DECIMAL(10, 2), nullable=False)
    observacao = Column(Text)
    itens_comprados = Column(Text)
    
    usuario_id = relationship("Usuario")
    
    def __repr__(self):
        return (
            f"<Pedido(id={self.id}, "
            f"usuario_id={self.usuario_id}, "
            f"data_pedido={self.data_pedido}, "
            f"forma_pagamento='{self.forma_pagamento}', "
            f"endereco_entrega='{self.endereco_entrega}', "
            f"status='{self.status}', "
            f"valor_total={self.valor_total}, "
            f"observacao='{self.observacao}', "
            f"itens_comprados='{self.itens_comprados}')>"
        )



if __name__ == "__main__":
    # Associar o engine ao metadata da Base
    Base.metadata.create_all(bind=engine)
