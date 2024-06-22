# Começando o Projeto e Importações

## Bibliotecas Utilizadas e Versões

- Flask-RESTful==0.3.10
- requests==2.32.3
- SQLAlchemy==2.0.31
- Flask==3.0.3
- bcrypt

Para instalar todas as dependências listadas, utilize o seguinte comando:

```bash```
pip install -r requirements.txt


## Conexão com o Banco esta no Model no CreateSQL: 

Nesse arquiso esta a conexão com o banco e o tipo do Banco de dados 

## Estrutura de Pagina, ela segue uma estrutura MVC: 

## MODEL é a definição da classe do objeto junto ao ORM do SQLALCHEMY

Aqui eu faço todo o mapeamento do objeto com e com suas tabelas defininando suas caracteristica.
Essas classes são mapeadas diretamente para tabelas no banco de dados.

## Controller eu defino as rotas de acesso, e as validações que em breve sera feita por uma api

O Controller é responsável por definir as rotas de acesso (endpoints) e por conter a lógica de validação e processamento das requisições.
Em breve sera a API responsavel por fazer todo esse controller

## View é a visualização da pagina com os templates que o Flask consegue Carrega:

Aqui a view esta na pasta template aonde eu separo o Cliente do Admin 


