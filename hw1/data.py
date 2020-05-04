# coding=utf-8
import pickle

if __name__ == "__main__":
    with open("world.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    data = []
    for line in lines[1:]:
        data.append(line.strip().split(","))

    # timeline
    c1 = data[0][1]
    l = 0
    timeline = []
    for d in data:
        if d[1] == c1:
            l += 1
            timeline.append(d[0])

    # country
    country = [c1]
    country_index = {c1: 0}
    for i in range(1, len(data)):
        if data[i][1] != data[i-1][1]:
            country_index[data[i][1]] = len(country)
            country.append(data[i][1])

    # confirm
    confirm = [[] for _ in country]
    for d in data:
        confirm[country_index[d[1]]].append(int(d[2]))

    # dead
    dead = [[] for _ in country]
    for d in data:
        dead[country_index[d[1]]].append(int(d[4]))

    # avail
    avail = [[] for _ in country]
    for d in data:
        avail[country_index[d[1]]].append(int(d[8]))

    with open("data.pkl", "wb") as f:
        pickle.dump([timeline, country, country_index, confirm, dead, avail], f)
