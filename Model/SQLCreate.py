from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# Configurações do banco de dados MySQL
USER = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'
DATABASE = 'olimpico'

# Criar a URL de conexão para MySQL
DATABASE_URL = URL.create(
    drivername="mysql+mysqlconnector",
    username=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE,
)

try:
    # Criar o engine de conexão
    engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver as queries executadas
    
    # Testar a conexão
    with engine.connect() as connection:
        print("Conexão bem-sucedida!")

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {str(e)}")
