from flask import Blueprint, render_template, redirect, url_for

page_bp = Blueprint('page_bp', __name__)

@page_bp.route('/')
def index():
    print("Acessando a rota /")
    return render_template("index.html")

@page_bp.route("/login")
def login():
    print("Acessando a rota /login")
    return render_template('login.html')

@page_bp.route("/cadastro")
def cadastro():
    print("Acessando a rota /cadastro")
    return render_template('cadastro.html')

@page_bp.route("/cadastro_admin")
def cadastro_admin():
    print("Acessando a rota /cadastro_admin")
    return render_template('cadastro_admin.html')

@page_bp.route("/produto")
def produto():
    print("Acessando a rota /produto")
    return render_template('./admin/newproduto.html')

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
    return render_template('/admin/base.html')
