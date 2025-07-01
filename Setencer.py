pesquisa = "Quero aprender Flask para criar uma API"

setencas = [
    "Como aprender Python para iniciantes em 30 dias",
    "Tutorial de JavaScript para criar sites interativos",
    "Guia completo de Flask para desenvolvimento web",
    "Introdução ao Java para programação backend",
    "Dicas para melhorar suas habilidades em programação"
]

from sentence_transformers import CrossEncoder
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

pontuacao = model.predict([(pesquisa, s) for s in setencas])
print(pontuacao)