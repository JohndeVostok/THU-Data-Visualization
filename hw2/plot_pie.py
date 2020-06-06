import json
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Pie

DATA_FILE = "imdb_data.json"


if __name__ == "__main__":
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    genres = data["genres"]
    meta_data = [[] for _ in genres]
    for movie in data["movies"]:
        for idx, flag in enumerate(movie["genre"]):
            if flag:
                meta_data[idx].append({"title": movie["title"], "rating": movie["rating"]})

    data_pair = []
    tooltip = {}
    for i in range(len(genres)):
        data_pair.append([genres[i], len(meta_data[i])])
        tmp = sorted([[t["title"].replace("\"", "*").replace("\'", "+"), t["rating"]] for t in meta_data[i]], key=lambda t:t[1], reverse=True)[:5]
        tooltip[genres[i]] = tmp
    tooltip_json = json.dumps(tooltip)
    print(tooltip["Drama"])

    pie = Pie()
    pie.add_js_funcs("data = JSON.parse(\'" + tooltip_json + "\');")
    pie.add(
        series_name="",
        data_pair=data_pair,
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            formatter=JsCode("function(params){ text = \'\'; reg1 = new RegExp(\'\\*\' , \'g\'); reg2 = new RegExp(\'\\+\', \'g\'); for (i = 0; i < 5; i++) { title = data[params.name][i][0]; title = title.replace(reg1, \'&quot\'); title = title.replace(reg2, \'&apos\'); rating = data[params.name][i][1]; text += title + \': \' + rating + '<br>'}; return text;}")
        )
    )
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="IMDB Pie"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    pie.render()
