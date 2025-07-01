import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def converterJsonParaLista(objetoJson):
    objetoDict = objetoJson
    try:
        frase = ""
        for i, v in enumerate(objetoDict.items()):
            frase = v[1]
        return frase
    except:
        return "Algo deu errado"

def tratamentoDeTexto(pesquisa):
    pesquisa = pesquisa.lower()
    listaDePalavras = word_tokenize(pesquisa, language='portuguese')
    stopWordsPortuguese = stopwords.words('portuguese')
    for i in listaDePalavras:
        for n in stopWordsPortuguese:
            if i == n:
                listaDePalavras.remove(n)
    listaDePalavras = [item for item in listaDePalavras if item not in string.punctuation]
    listaDePalavras = ' '.join(listaDePalavras)

    return listaDePalavras
    


