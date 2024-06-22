from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from dao.UsuarioAdminDAO import UsuarioAdminDAO
from dao.UsuarioDAO import UsuarioDAO
from Model.UsuarioSQL import Usuario

# Criar instância do Blueprint para usuários
user_bp = Blueprint('user_bp', __name__)

# Criar instâncias dos DAOs
usuario_admin_dao = UsuarioAdminDAO()
usuario_dao = UsuarioDAO()

@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Pegar dados do formulário
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmacaoSenha = request.form.get('confirmacaoSenha')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        numero_casa = request.form.get('numero_casa')
        complemento = request.form.get('complemento')
        bairro = request.form.get('bairro')

        # Verificar se as senhas correspondem
        if senha != confirmacaoSenha:
            flash('As senhas não correspondem', 'error')
            return redirect(url_for('user_bp.register'))

        # Verificar se email já está cadastrado
        if usuario_dao.obter_por_email(email):
            flash('Email já cadastrado', 'error')
            return redirect(url_for('user_bp.register'))
        
        # Verificar se telefone já está cadastrado
        if usuario_dao.obter_por_telefone(telefone):
            flash('Telefone já cadastrado', 'error')
            return redirect(url_for('user_bp.register'))

        # Criar instância do usuário
        usuario = Usuario(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            senha=senha,  # Armazenar a senha como uma string sem hash
            telefone=telefone,
            endereco=endereco,
            tipo_usuario = 'Cliente',
            numero_casa=numero_casa,
            complemento=complemento,
            bairro=bairro
        )
        
        try:
            # Salvar no banco de dados
            usuario_dao.incluir(usuario)
            flash('Usuário registrado com sucesso!', 'success')
            return redirect(url_for('user_bp.login'))  # Redirecionar para a página de login após o registro
        except Exception as e:
            flash(f'Erro ao registrar usuário: {str(e)}', 'error')
            return redirect(url_for('user_bp.register'))

    # Se o método HTTP não for POST (pode ser GET), renderize o formulário de registro
    return render_template('cadastro.html')


@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Verificar se o usuário existe no banco de dados
        usuario = usuario_dao.obter_por_email(email)

        if usuario:
            # Verificar se a senha está correta
            if senha == usuario.senha:
                # Autenticar usuário
                session['usuario_id'] = usuario.id
                session['usuario_nome'] = usuario.nome
                session['tipo_usuario'] = usuario.tipo_usuario  # Adiciona o tipo de usuário à sessão

                flash('Login realizado com sucesso!', 'success')

                # Redirecionar com base no tipo de usuário
                if usuario.tipo_usuario == 'Administrador':
                    return redirect(url_for('admin.dashboard'))
                else:
                    return redirect(url_for('page_bp.index'))
            else:
                flash('Credenciais inválidas. Verifique seu email e senha.', 'error')
                return redirect(url_for('user_bp.login'))
        else:
            flash('Usuário não encontrado. Verifique seu email e senha.', 'error')
            return redirect(url_for('user_bp.login'))

    # Se o método HTTP for GET, renderize o formulário de login
    return render_template('login.html')

@user_bp.route('/logout')
def logout():
    # Limpar sessão
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('page_bp.index'))
