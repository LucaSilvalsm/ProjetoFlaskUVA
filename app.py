from flask import Flask
from controller.page_controller import page_bp
from controller.UsuarioController import user_bp
from controller.AdminController import admin_bp
from controller.ProdutoController import produto_bp  # Certifique-se de importar produto_bp
import secrets

app = Flask(__name__)

# Configuração da chave secreta
app.secret_key = secrets.token_hex(24)

# Registrar os blueprints com seus prefixos correspondentes
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(page_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(produto_bp, url_prefix='/produto')  # Registrando produto_bp com prefixo '/produto'

# Rota de teste para verificar se o servidor está funcionando
@app.route('/test')
def test():
    return "Servidor funcionando!"

if __name__ == '__main__':
    app.run(debug=True)
