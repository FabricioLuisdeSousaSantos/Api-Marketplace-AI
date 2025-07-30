from sqlalchemy import create_engine, text

class Banco:
    def __init__(self, _nomeTabela, _nomeBanco):
        self.nomeTabela  = _nomeTabela
        self.nomeBanco   = _nomeBanco 
        self.motor       = create_engine(f"mysql+pymysql://root:@localhost:3306/{self.nomeBanco}")
    
    def testarConexao(self):
        try:
            with self.motor.connect() as conexao:
                resultado = conexao.execute(text(f"SELECT * FROM {self.nomeTabela}"))
                for linha in resultado:
                    print(linha)
        except Exception as erro:
            print(f"Erro: {erro}")
    
    def retornarSentencas(self):
        setencas = []
        try:
            with self.motor.connect() as conexao:
                resultado = conexao.execute(text(f"SELECT nome FROM {self.nomeTabela}"))
                for linha in resultado:
                    setencas.append(''.join(linha))
                return setencas
        except Exception as erro:
            print(f"Erro: {erro}")


b1 = Banco("grupopesquisa", "ai_marktingplace")
b1.retornarSentencas()







