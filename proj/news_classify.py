import json



if __name__ == "__main__":
    with open("news_data.json", "r") as f:
        data = json.load(f)
    with open("news_classifier.json", "r") as f:
        classifier = json.load(f)
    res = {}
    for date in data:
        tags = []
        for news in data[date]:
            cut = news["news_cut"]
            flag = [0 for _ in range(2)]
            for key in classifier:
                if flag[classifier[key]-1]:
                    continue
                if key in cut:
                    flag[classifier[key]-1] = 1
            tags.append(2 * flag[1] + flag[0])
        res[date] = tags

    with open("news_classify.json", "w") as f:
        json.dump(res, f)