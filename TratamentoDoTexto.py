import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

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
    


