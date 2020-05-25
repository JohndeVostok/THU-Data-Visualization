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
    
    with open("stopword.json", "r") as f:
        stop_word = json.load(f)
    with open("keyword.json", "r") as f:
        key_word = json.load(f)

    final_data = {}
    for date in data:
        try:
            with open(data[date]["news_file"], "r") as f:
                news = json.load(f)
            with open(data[date]["comment_file"], "r") as f:
                comment = json.load(f)
        except Exception as e:
            continue

        meta_data = []

        for i in range(len(news)):
            if i % 100 == 0:
                print(date + " : " + str(i) + "/" + str(len(news)))
            news_title = news[i]["title"]
            news_content = news[i]["meta"]["content"]
            news_cut_tmp = jieba.lcut(news_content)
            news_cut = []

            flag = False
            for word in key_word:
                if word in news_cut_tmp:
                    flag = True
                    break

            if flag:
                for word in news_cut_tmp:
                    if word not in stop_word:
                        news_cut.append(word)
                tmp = {}
                tmp["title"] = news_title
                tmp["news"] = news_content
                tmp["news_cut"] = news_cut
                tmp["comment_num"] = 0
                meta_data.append(tmp)

        title = [tmp["title"] for tmp in meta_data]
        for i in range(len(comment)):
            comment_title = comment[i]["title"]
            comment_num = len(comment[i]["comment"])

            if comment_title not in title:
                continue
            idx = title.index(comment_title)
            meta_data[idx]["comment_num"] = comment_num

        final_data[date] = meta_data
        print("Finish: " + date + " : " + str(len(meta_data)))

    with open("news_data.json", "w") as f:
        json.dump(final_data, f)

