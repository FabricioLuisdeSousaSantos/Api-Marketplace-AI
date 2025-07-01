from flask import Flask, request
import TratamentoDoTexto
import Recomendador

app = Flask(__name__)

@app.route('/')
def home():
    return ''

@app.route('/api/enviarPesquisas', methods=['POST'])
def processarPesquisas():
    dados = request.get_json()
    frase = TratamentoDoTexto.converterJsonParaLista(dados)
    fraseTratada  = TratamentoDoTexto.tratamentoDeTexto(frase)
    recomendacao  = Recomendador.predicao(fraseTratada)
    return recomendacao

app.run(debug=True)

