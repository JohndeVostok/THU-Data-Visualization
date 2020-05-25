#coding=utf-8
import os
import sys
import csv
import json
import pickle

if __name__ == "__main__":
    csv.field_size_limit(sys.maxsize)
    files = os.listdir("data")
    file_list = []
    for filename in files:
        if filename.split('.')[-1] == "pkl":
            s = "data/" + filename
            file_list.append(s)

    data = {}
    for file_name in file_list:
        print("Processing: ", file_name)
        with open(file_name, "rb") as f:
            tmp = pickle.load(f)
        data.update(tmp)

    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    for key in data:
        print(key)

