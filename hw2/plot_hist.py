import json
from pyecharts import options as opts
from pyecharts.charts import Bar

DATA_FILE = "imdb_data.json"

if __name__ == "__main__":
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    genres = data["genres"]
    min_year = 2000
    max_year = 1000
    for movie in data["movies"]:
        if movie["year"] != -1:
            min_year = min([min_year, movie["year"]])
            max_year = max([max_year, movie["year"]])
    # print(min_year, max_year)
    base_year = int(min_year / 10) * 10
    num_year = int((int(max_year / 10) * 10 - base_year) / 10 + 1)
    # print(base_year, num_year)
    meta_data = [[0 for _ in range(num_year)] for _ in genres]
    for movie in data["movies"]:
        if movie["year"] == -1:
            continue
        decade_id = int((movie["year"] - base_year) / 10)
        for idx, flag in enumerate(movie["genre"]):
            if flag:
                meta_data[idx][decade_id] += 1

    # print(meta_data)

    bar = Bar()
    decades = []
    for i in range(num_year):
        decades.append(str(base_year + 10 * i) + "-" + str(base_year + 10 * i + 9))
    bar.add_xaxis(decades)
    for idx, genre in enumerate(genres):
        bar.add_yaxis(
            genre,
            meta_data[idx],
            stack="stack1",
            category_gap="50%",
            label_opts=opts.LabelOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
            )
        )
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="IMDB Stacked Hist"),
        legend_opts=opts.LegendOpts(type_="scroll", is_show=True, pos_bottom="bottom")
    )
    bar.render("hist.html")
