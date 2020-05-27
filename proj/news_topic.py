import json
import math

if __name__ == "__main__":
    with open("news_data.json", "r") as f:
        data = json.load(f)
    
    tfidf = {}
    for date in data:
        meta_data = data[date]
        term_list = [doc["news_cut"] for doc in meta_data]
        doc_num = len(term_list)
        tf = [{} for _ in range(doc_num)]
        idf = {}
        for i in range(doc_num):
            terms = term_list[i]
            term_num = len(terms)
            tmp = {}
            for term in terms:
                if term not in tf[i]:
                    tf[i][term] = 0
                tf[i][term] += 1 / term_num
                if term not in tmp:
                    tmp[term] = 1
            for term in tmp:
                if term not in idf:
                    idf[term] = 0
                idf[term] += 1
        
        for term in idf:
            idf[term] = math.log(doc_num / (idf[term] + 1))

        res = []
        for i in range(doc_num):
            for term in tf[i]:
                tf[i][term] *= idf[term]
            res.append(sorted(tf[i].items(), key=lambda d:d[1], reverse=True))
        tfidf[date] = res
        print("finish: ", date)
    with open("news_tfidf.json", "w") as f:
        json.dump(tfidf, f)

