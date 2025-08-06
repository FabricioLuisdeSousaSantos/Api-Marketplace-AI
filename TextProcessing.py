import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

class TextProcessing:
    def convertJsonToArray(JsonObj) -> str:
        objDict = JsonObj
        try:
            phase = ""
            for i, v in enumerate(objDict.items()):
                phase = v[1]
            return phase
        except:
            return "Something went wrong!"
    
    def textCleaning(_search) -> list:
        search              = _search.lower()
        searchTokenizer     = word_tokenize(search, language='portuguese')
        stopWordsPortuguese = stopwords.words('portuguese')
        for t in searchTokenizer:
            for sw in stopWordsPortuguese:
                if t == sw:
                    searchTokenizer.remove(sw)
        searchTokenizer = [item for item in searchTokenizer if item not in string.punctuation]
        searchTokenizer = ' '.join(searchTokenizer)

        return searchTokenizer
