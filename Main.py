from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo à minha API Flask!'

@app.route('/api/enviarPesquisas', methods=['POST'])
def processarPesquisas():
    data = request.get_json()
    return data

if __name__ == '__main__':
    app.run(debug=True)