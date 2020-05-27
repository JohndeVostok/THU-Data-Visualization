import json

NUM_KEY = 20

if __name__ == "__main__":
    with open("news_tfidf.json", "r") as f:
        data = json.load(f)
    res_cnt = []
    res_tfidf = []
    for date in data:
        tmp_cnt = {}
        tmp_tfidf = {}
        tfidf = data[date]
        for terms in tfidf:
            for k, _ in terms[:NUM_KEY]:
                if k not in tmp_cnt:
                    tmp_cnt[k] = 0
                tmp_cnt[k] += 1
            for k, v in terms:
                if k not in tmp_tfidf:
                    tmp_tfidf[k] = 0
                tmp_tfidf[k] += v
        tmp = sorted(tmp_cnt.items(), key=lambda d:d[1], reverse=True)
        res_cnt.append(date + "," + ",".join([str(t) for t in tmp[:NUM_KEY]]) + "\n")
        tmp = sorted(tmp_tfidf.items(), key=lambda d:d[1], reverse=True)
        res_tfidf.append(date + "," + ",".join([str(t) for t in tmp[:NUM_KEY]]) + "\n")
        print("finish: ", date)

    with open("news_topic_cnt.csv", "w") as f:
        f.writelines(res_cnt)
    with open("news_topic_tfidf.csv", "w") as f:
        f.writelines(res_tfidf)
