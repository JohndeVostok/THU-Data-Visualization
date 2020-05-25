#coding=utf-8
import os
import json
import jieba

if __name__ == "__main__":
    file_list = os.listdir("news_data/data")
    data = {}
    for filename in file_list:
        date = filename.split(".")[0]
        if date not in data:
            data[date] = {}
        data[date]["news_file"] = "news_data/data/" + filename
        data[date]["comment_file"] = "news_data/comment/" + filename

    data = dict(sorted(data.items(), key=lambda d:d[0]))

    for date in data:
        print("Processing: " + date)
        try:
            with open(data[date]["news_file"], "r") as f:
                news = json.load(f)
            with open(data[date]["comment_file"], "r") as f:
                comment = json.load(f)
            data[date]["flag"] = True
        except Exception as e:
            print("ERROR: " + date + " " + str(e))
            data[date]["flag"] = False
            continue

        data[date]["title"] = []
        data[date]["news"] = []
        data[date]["comment"] = []
        data[date]["news_cut"] = []
        data[date]["comment_cut"] = []

        for i in range(len(news)):
            data[date]["title"].append(news[i]["title"])
            data[date]["news"].append(news[i]["meta"]["content"])
            data[date]["news_cut"].append(jieba.lcut(news[i]["meta"]["content"]))
            data[date]["comment"].append([])
            data[date]["comment_cut"].append([])
        for i in range(len(comment)):
            if comment[i]["title"] not in data[date]["title"]:
                continue
            idx = data[date]["title"].index(comment[i]["title"])
            for tmp in comment[i]["comment"]:
                data[date]["comment"][idx].append(tmp["content"])
                data[date]["comment_cut"][idx].append(jieba.lcut(tmp["content"]))
    with open("news_data.json", "w") as f:
        json.dump(data, f)

