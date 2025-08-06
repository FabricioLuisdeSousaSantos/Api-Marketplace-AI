from flask import Flask, request
from TextProcessing import TextProcessing
from Recommender import Recommender

app    = Flask(__name__)
recomm = Recommender()

@app.route('/')
def home():
    return ''

@app.route('/sendSearches', methods=['POST'])
def process():
    data               = request.get_json()
    phase              = TextProcessing.convertJsonToArray(data)
    processedSentence  = TextProcessing.textCleaning(phase)
    recommendation     = recomm.predictWithModel(processedSentence)  
    return recommendation

app.run(debug=True)

