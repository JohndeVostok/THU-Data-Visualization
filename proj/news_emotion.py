import requests
import json
import time

ACCESS_TOKEN_URL = "https://aip.baidubce.com/oauth/2.0/token"
EMOTION_URL = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify"

def get_emotion(text, url):
    try:
        data = json.dumps({"text": text}).encode("utf-8")
        resp = requests.post(url=url, data=data)
        res = json.loads(resp.text)
    except:
        return -1
    if "items" not in res:
        return -1
    else:
        return res["items"][0]["sentiment"]

def get_corp(text):
    l = len(text)
    if l > 1024:
        st = int((l - 1024) / 2)
        return text[st:st+1024]
    else:
        return text

if __name__ == "__main__":
    with open("baidu_cloud_config.json", "r") as f:
        conf = json.load(f)
    url = ACCESS_TOKEN_URL + "?grant_type={}&client_id={}&client_secret={}".format(conf["grant_type"], conf["client_id"], conf["client_secret"])
    resp = requests.post(url)
    tmp = json.loads(resp.text)
    access_token = tmp["access_token"]
    
    url = EMOTION_URL + "?charset=UTF-8&access_token={}".format(access_token)
    with open("news_data.json", "r") as f:
        data = json.load(f)
    res = {}
    for date in data:
        print(date)
        res[date] = []
        meta_list = data[date]
        for idx, meta in enumerate(meta_list):
            if idx % 100 == 0:
                print(idx, "/", len(meta_list))
            text = get_corp(meta["news"])
            retry = 3
            while retry > 0:
                emotion = get_emotion(text, url)
                if emotion != -1:
                    break
                retry -= 1
                time.sleep(0.05)
            res[date].append(emotion)
    with open("news_emotion.json", "w") as f:
        json.dump(res, f)
