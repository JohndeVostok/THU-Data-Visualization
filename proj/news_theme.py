import json

if __name__ == "__main__":
    with open("news_type.json", "r") as f:
        news_type = json.load(f)
    with open("news_wc.json", "r") as f:
        news_wc = json.load(f)

    wc_global = [{} for i in range(5)]
    
    for date in news_wc:
        for idx in range(len(news_wc[date])):
            wc = news_wc[date][idx]
            ts = news_type[date][idx]
            for t in ts:
                for w in wc:
                    if w not in wc_global[t]:
                        wc_global[t][w] = 0
                    wc_global[t][w] += wc[w]
                    if w not in wc_global[-1]:
                        wc_global[-1][w] = 0
                    wc_global[-1][w] += wc[w]

    themes = []
    for i in range(5):
        tmp = sorted(wc_global[i].items(), key=lambda d:d[1], reverse=True)
        themes.append([d[0] for d in tmp[:50]])

    res = {}
    for date in news_wc:
        tmp_wc = [{} for i in range(5)]
        for idx in range(len(news_wc[date])):
            wc = news_wc[date][idx]
            ts = news_type[date][idx]
            for t in ts:
                for w in wc:
                    if w not in tmp_wc[t]:
                        tmp_wc[t][w] = 0
                    tmp_wc[t][w] += wc[w]
                    if w not in tmp_wc[-1]:
                        tmp_wc[-1][w] = 0
                    tmp_wc[-1][w] += wc[w]
        
        res[date] = []
        for idx, theme_list in enumerate(themes):
            res[date].append([])
            for theme in theme_list:
                # print(theme, tmp_wc[idx][theme])
                if theme in tmp_wc[idx]:
                    res[date][idx].append([theme, tmp_wc[idx][theme]])
                else:
                    res[date][idx].append([theme, 0])

    with open("news_theme.json", "w") as f:
        json.dump(res, f)