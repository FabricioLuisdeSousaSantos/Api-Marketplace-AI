from sentence_transformers import CrossEncoder
import numpy as np
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
from BancoDeDados import Banco

setencas = Banco("grupopesquisa", "ai_marktingplace").retornarSentencas();

def predicao(pesquisa):
    pontuacao = model.predict([(pesquisa, s) for s in setencas])
    indicesOrdenados = np.argsort(pontuacao)[::-1]
    tres_maiores_indices = indicesOrdenados[:3]
    resultados = [(setencas[i], float(pontuacao[i])) for i in tres_maiores_indices]
    return resultados



    


   