from sqlalchemy.orm import Session
from sqlalchemy import select, update
from Model.UsuarioSQL import UsuarioAdmin, engine

class UsuarioAdminDAO:
    def __init__(self):
        self.session = Session(engine)
    
    def incluir(self, usuario_admin):
        self.session.add(usuario_admin)
        self.session.commit()
        return usuario_admin
   
    def alterar(self, usuario_admin):
        self.session.execute(update(UsuarioAdmin).where(UsuarioAdmin.id == usuario_admin.id).values(
            nome=usuario_admin.nome,
            sobrenome=usuario_admin.sobrenome,
            email=usuario_admin.email,
            tipo_usuario=usuario_admin.tipo_usuario,
            senha=usuario_admin.senha
        ))
        self.session.commit()
    
    def excluir(self, chave):
        usuario_admin = self.session.get(UsuarioAdmin, chave)
        if usuario_admin:
            self.session.delete(usuario_admin)
            self.session.commit()
    
    def obterTodos(self):
        stmt = select(UsuarioAdmin)
        result = self.session.scalars(stmt).all()
        return result
    
    def obter(self, chave):
        return self.session.get(UsuarioAdmin, chave)
    
    def obter_por_email(self, email):
        return self.session.query(UsuarioAdmin).filter_by(email=email).first()
