import json
from gensim import corpora, models

if __name__ == "__main__":
    with open("news_data.json", "r") as f:
        data = json.load(f)
    
    for date in data:
        meta_data = data[date]
        term_list = [doc["news_cut"] for doc in meta_data]
        dic = corpora.Dictionary(term_list)
        corp = [dic.doc2bow(terms) for terms in term_list]
        lda = models.ldamodel.LdaModel(corpus=corp, id2word=dic, num_topics=10)
        print(lda.inference(corp))

