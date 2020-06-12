import json


if __name__ == "__main__":
    with open("news_type_keyword.json", "r") as f:
        tmp = json.load(f)
    types = tmp["types"]
    keyword = tmp["keyword"]

    with open("news_data.json", "r") as f:
        data = json.load(f)

    news_type = {}

    word_count = {}

    for date in data:
        print(date)
        news_type[date] = []
        word_count[date] = []
        meta_list = data[date]
        for idx, meta in enumerate(meta_list):
            if idx % 100 == 0:
                print(idx, "/", len(meta_list))
            tmp_wc = {}
            for word in meta["news_cut"]:
                if word not in tmp_wc:
                    tmp_wc[word] = 0
                tmp_wc[word] += 1
            word_count[date].append(tmp_wc)
            tmp = []
            for i in range(len(types)):
                flag = False
                for word in tmp_wc:
                    if word in keyword[i]:
                        tmp.append(i)
                        flag = True
                        break
                if flag:
                    continue
            news_type[date].append(tmp)

    with open("news_type.json", "w") as f:
        json.dump(news_type, f)
    with open("news_wc.json", "w") as f:
        json.dump(word_count, f)