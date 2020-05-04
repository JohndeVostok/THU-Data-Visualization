import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pickle
from colorlist import cnames

if __name__ == "__main__":
    with open("data.pkl", "rb") as f:
        [timeline, country, country_index, confirm, dead, avail] = pickle.load(f)

    clist = []
    for c in cnames:
        clist.append(c)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    
    plt.figure(figsize=(8, 3))
    plt.subplot(122)
    plt.axis("off")
    plt.legend(handles=[mpatches.Patch(label=country[i], color=clist[i]) for i in range(len(country))], ncol=3)
    plt.subplot(121)
    for i in range(63):
        plt.cla()
        plt.xlim(0, 64)
        plt.xlabel("day")
        plt.ylabel("confirm")
        for j in range(len(country)):
            c = country[j]
            plt.plot(range(i+1), confirm[country_index[c]][:i+1], color=clist[j])
        plt.pause(0.1)
    plt.show()
