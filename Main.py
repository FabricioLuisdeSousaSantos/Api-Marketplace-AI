from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo à minha API Flask!'

@app.route('/api/enviarPesquisas', methods=['POST'])
def enviar():
    data = request.get_json()
    return ''


@app.route('/api/receberRecomendacoes', methods=['GET'])
def enviar():
    pass







if __name__ == '__main__':
    app.run(debug=True)