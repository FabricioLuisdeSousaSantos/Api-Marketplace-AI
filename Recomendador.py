from sentence_transformers import CrossEncoder
import numpy as np
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

setencas = [
    "Como aprender Python para iniciantes em 30 dias",
    "Tutorial de JavaScript para criar sites interativos",
    "Guia completo de Flask para desenvolvimento web",
    "Introdução ao Java para programação backend",
    "Dicas para melhorar suas habilidades em programação"
]

def predicao(pesquisa):
    pontuacao = model.predict([(pesquisa, s) for s in setencas])
    indicesOrdenados = np.argsort(pontuacao)[::-1]
    tres_maiores_indices = indicesOrdenados[:3]
    resultados = [(setencas[i], float(pontuacao[i])) for i in tres_maiores_indices]
    return resultados



    


   