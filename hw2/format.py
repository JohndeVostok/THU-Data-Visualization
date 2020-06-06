import csv
import json

IMDB_FILE = "imdb.csv"
DATA_FILE = "imdb_data.json"

if __name__ == "__main__":
    lines = []
    with open(IMDB_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for line in reader:
            lines.append(line)
    
    genres = header[16:]
    movies = []
    for line in lines:
        movie = {}
        movie["title"] = line[2]
        try:
            movie["rating"] = float(line[5])
        except:
            movie["rating"] = -1
        movie["genre"] = [int(t) for t in line[16:]]
        movies.append(movie)

    data = {}
    data["genres"] = genres
    data["movies"] = movies
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
