from flask import Flask, request
import TratamentoDoTexto

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo à minha API Flask!'

@app.route('/api/enviarPesquisas', methods=['POST'])
def processarPesquisas():
    data = request.get_json()
    print(TratamentoDoTexto.converterJsonParaLista(data))
    return data

app.run(debug=True)