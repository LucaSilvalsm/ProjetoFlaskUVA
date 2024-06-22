from sqlalchemy import select, update
from sqlalchemy.orm import Session

from Model.Produtos import Produto, engine
import secrets

class ProdutoDAO:
    def __init__(self):
        self.session = Session(engine)
    
    def incluir(self, produto):
        self.session.add(produto)
        self.session.commit()
        return produto
   
    def alterar(self, produto):
        self.session.execute(update(Produto).where(Produto.id == produto.id).values(
            nome_produto=produto.nome_produto,
            tipo_produto=produto.tipo_produto,
            tamanho=produto.tamanho,
            ingrediente=produto.ingrediente,
            preco=produto.preco,
            descricao=produto.descricao,
            imagem=produto.imagem  # Corrigido de `produto.image` para `produto.imagem`
        ))
        self.session.commit()
    
    def excluir(self, chave):
        produto = self.session.get(Produto, chave)
        if produto:
            self.session.delete(produto)
            self.session.commit()
    
    def obter_todos(self):
        stmt = select(Produto)
        result = self.session.execute(stmt).scalars().all()  # Corrigido de `self.session.scalars(stmt).all()` para `self.session.execute(stmt).scalars().all()`
        return result
    
    def tipo_produto(self, tipo_produto):
        stmt = select(Produto).where(Produto.tipo_produto == tipo_produto)
        result = self.session.execute(stmt).scalars().all()  # Corrigido de `self.session.scalars(stmt).all()` para `self.session.execute(stmt).scalars().all()`
        return result
    
    def obter(self, chave):
        return self.session.get(Produto, chave)
    
    def image_generate_name(self):
        return secrets.token_hex(60) + ".jpg"
    
    def close(self):
        self.session.close()

# Testando a função image_generate_name e tipo_produto
if __name__ == "__main__":
    produto_dao = ProdutoDAO()
    
    generated_name = produto_dao.image_generate_name()
    print(f"Generated image name: {generated_name}")
    
    tipo_produto_result = produto_dao.tipo_produto("Hambúrguer Artesanal")
    for produto in tipo_produto_result:
        print(produto)
    
    # Fechar a sessão
    produto_dao.close()
