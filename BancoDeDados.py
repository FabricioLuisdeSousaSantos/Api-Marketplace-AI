from sqlalchemy import create_engine, text, MetaData, select, Table
from dotenv import load_dotenv
import os

db_host     = os.getenv("DB_HOST")
db_port     = os.getenv("DB_PORT")
db_name     = os.getenv("DB_NAME")
db_user     = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

class Banco:
    def __init__(self, _nomeTabela, _nomeBanco):
        self.nomeTabela  = _nomeTabela
        self.nomeBanco   = _nomeBanco 
        self.motor       = create_engine(f"mysql+pymysql://root:@localhost:3306/{self.nomeBanco}")
        self.metadata    = MetaData()
        self.tabela      = Table(self.nomeTabela, self.metadata, autoload_with=self.motor)
    
    def testarConexao(self):
        try:
            with self.motor.connect() as conexao:
                resultado = conexao.execute(select(self.tabela.c.nome))
                for linha in resultado:
                    print(linha)
        except Exception as erro:
            print(f"Erro: {erro}")
    
    def retornarSentencas(self):
        setencas = []
        try:
            with self.motor.connect() as conexao:
                resultado = conexao.execute(select(self.tabela.c.nome))
                for linha in resultado:
                    setencas.append(''.join(linha))
                return setencas
        except Exception as erro:
            print(f"Erro: {erro}")









