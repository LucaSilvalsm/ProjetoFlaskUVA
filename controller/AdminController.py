from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from dao.UsuarioAdminDAO import UsuarioAdminDAO
from Model.UsuarioSQL import UsuarioAdmin

admin_bp = Blueprint('admin_bp', __name__)

# Criar instância do DAO
usuario_admin_dao = UsuarioAdminDAO()

@admin_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Pegar dados do formulário
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmacaoSenha = request.form.get('confirmacaoSenha')

        # Verificar se as senhas correspondem
        if senha != confirmacaoSenha:
            flash('As senhas não correspondem', 'error')
            return redirect(url_for('admin_bp.register'))

        # Verificar se email já está cadastrado
        if usuario_admin_dao.obter_por_email(email):
            flash('Email já cadastrado', 'error')
            return redirect(url_for('admin_bp.register'))

        # Criar instância do usuário administrador
        usuario_admin = UsuarioAdmin(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            tipo_usuario='Administrador',
            senha=senha  # Armazenar a senha como uma string sem hash
        )

        try:
            # Salvar no banco de dados
            usuario_admin_dao.incluir(usuario_admin)
            flash('Usuário administrador registrado com sucesso!', 'success')
            return redirect(url_for('admin_bp.login'))  # Redirecionar para a página de login após o registro
        except Exception as e:
            flash(f'Erro ao registrar usuário administrador: {str(e)}', 'error')
            return redirect(url_for('admin_bp.register'))

    # Se o método HTTP não for POST (pode ser GET), renderize o formulário de registro
    return render_template('cadastro_admin.html')

@admin_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Verificar se o usuário administrador existe no banco de dados
        usuario_admin = usuario_admin_dao.obter_por_email(email)

        if usuario_admin:
            # Verificar se a senha está correta
            if senha == usuario_admin.senha:
                # Autenticar usuário administrador
                session['usuario_id'] = usuario_admin.id
                session['usuario_nome'] = usuario_admin.nome
                session['tipo_usuario'] = 'Administrador'

                flash('Login de administrador realizado com sucesso!', 'success')
                return redirect(url_for('admin_bp.dashboard'))  # Redirecionar para o dashboard de administrador
            else:
                flash('Credenciais inválidas. Verifique seu email e senha.', 'error')
                return redirect(url_for('admin_bp.login'))
        else:
            flash('Usuário não encontrado. Verifique seu email e senha.', 'error')
            return redirect(url_for('admin_bp.login'))

    # Se o método HTTP for GET, renderize o formulário de login
    return render_template('login_adm.html')

@admin_bp.route('/dashboard')
def dashboard():
    # Verificar se o usuário é administrador
    if 'tipo_usuario' in session and session['tipo_usuario'] == 'Administrador':
        return render_template('/admin/painel.html')
    else:
        flash('Acesso negado.', 'error')
        return redirect(url_for('admin_bp.login'))
