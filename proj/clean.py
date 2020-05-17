import os
import csv
import json
import pickle

if __name__ == "__main__":
    files = os.listdir("weibo")
    file_list = []
    for filename in files:
        if filename.split('.')[-1] == "csv":
            s = "weibo/" + filename
            file_list.append(s)


    for file_name in file_list:
        data = {}
        print("Processing: ", file_name)
        lines = []
        with open(file_name, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                lines.append(line)
    
        line = lines[0]
        key_idx = line.index("主题词")
        date_idx = line.index("发布日期")
        for line in lines[1:]:
            try:
                key_word = json.loads(line[key_idx])
                date = line[date_idx]
                if date not in data:
                    data[date] = []
                data[date].append(key_word)
            except:
                print(line)
        with open(file_name + ".pkl", "wb") as f:
            pickle.dump(data, f)
        

