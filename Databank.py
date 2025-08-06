from sqlalchemy import create_engine, MetaData, select, Table
from dotenv import load_dotenv
import os

load_dotenv()

db_host     = os.getenv("DB_HOST")
db_port     = os.getenv("DB_PORT")
db_name     = os.getenv("DB_NAME")
db_user     = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

class DataBank:
    def __init__(self, _tableName, _bankName):
        self.tableName  = _tableName
        self.bankName   = _bankName
        self.engine     = create_engine(f"mysql+pymysql://root:@localhost:3306/{self.bankName}")
        self.metadata   = MetaData()
        self.table      = Table(self.tableName, self.metadata, autoload_with=self.engine)
    
    def returnSentences(self) ->  list:
        sentences = []
        try:
            with self.engine.connect() as conn:
                result = conn.execute(select(self.table.c.nome))
                for l in result:
                    sentences.append(''.join(l))
                return sentences
            
        except Exception as erro:
            print(f"Erro: {erro}")








