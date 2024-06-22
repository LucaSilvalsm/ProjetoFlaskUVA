from flask import Blueprint, render_template, redirect, url_for
from dao.ProdutoDAO import ProdutoDAO


page_bp = Blueprint('page_bp', __name__)

@page_bp.route('/')
def index():
    produto_dao = ProdutoDAO()  # Criar uma instância válida de ProdutoDAO
    artesanais = produto_dao.tipo_produto("Artesanal")  # Chamar o método tipo_produto com o tipo desejado
    tradicionais = produto_dao.tipo_produto("Tradicional")
    bebidas = produto_dao.tipo_produto("Bebida")
    porcao = produto_dao.tipo_produto("Porcao")
    print("Acessando a rota /")
    print(artesanais)  # Apenas para debug, para verificar se os produtos foram obtidos corretamente
    return render_template("index.html", artesanais=artesanais,tradicionais=tradicionais,bebidas=bebidas, porcao=porcao)  # Passar os produtos obtidos para o template


@page_bp.route("/login")
def login():
    print("Acessando a rota /login")
    return render_template('login.html')

@page_bp.route("/cadastro")
def cadastro():
    print("Acessando a rota /cadastro")
    return render_template('cadastro.html')


@page_bp.route("/cesta")
def cesta():
    print("Acessando a rota /cesta")
    return render_template('cesta.html')



@page_bp.route("/cadastro_admin")
def cadastro_admin():
    print("Acessando a rota /cadastro_admin")
    return render_template('cadastro_admin.html')

@page_bp.route("/produto")
def produto():
    print("Acessando a rota /produto")
    return render_template('./admin/newproduto.html')

@page_bp.route("/all_produtos")
def all_produtos():
    produto_dao = ProdutoDAO() 
    
    produtos = produto_dao.todas_categorias()
    print("Acessando a rota /all_produtos")
    return render_template('./admin/all_produtos.html',produtos=produtos)



@page_bp.route("/painel")
def painel():
    print("Acessando a rota /painel")
    return render_template('./admin/painel.html')

@page_bp.route("/admin_login")
def admin_login():
    print("Acessando a rota /admin_login")
    return render_template('login_adm.html')

@page_bp.route("/admin_register")
def admin_register():
    print("Acessando a rota /admin_register")
    return redirect(url_for('admin_bp.register'))  # Redirecione para admin_bp.register

@page_bp.route('/dashboard')
def dashboard():
    return render_template('/admin/painel.html')
