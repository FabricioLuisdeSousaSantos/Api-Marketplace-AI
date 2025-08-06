from sentence_transformers import CrossEncoder
import numpy as np
from Databank import DataBank

class Recommender:
    def __init__(self):
        self.model     = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
        self.sentences = DataBank("grupopesquisa", "ai_marktingplace").returnSentences()

    def predictWithModel(self, search):
        punctuation = self.model.predict([(search, s) for s in self.sentences])
        indexsSort  = np.argsort(punctuation)[::-1]
        rank03      = indexsSort[:3]
        results     = [(self.sentences[i], float(punctuation[i])) for i in rank03]
        return results 





    


   