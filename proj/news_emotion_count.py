import json

if __name__ == "__main__":
    with open("news_type.json", "r") as f:
        news_type = json.load(f)
    with open("news_emotion.json", "r") as f:
        news_emotion = json.load(f)
    
    date_list = []
    news_ec = [[[], [], []] for _ in range(5)]
    for date in news_type:
        date_list.append("2020-" + date)

    for date in news_emotion:
        for i in range(5):
            for j in range(3):
                news_ec[i][j].append(0)
        for idx, emotion in enumerate(news_emotion[date]):
            types = news_type[date][idx]
            news_ec[4][emotion][-1] += 1
            for i in types:
                news_ec[i][emotion][-1] += 1
    
    with open("news_emotion_count.json", "w") as f:
        json.dump(news_ec, f)