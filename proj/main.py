import json
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import ThemeRiver, WordCloud, Tab, Grid, Timeline, Bar, Line
from pyecharts.faker import Faker

THEME_DATA_FILE = "news_theme.json"

BLACK_LIST = ["2020", "2019", u"责任编辑"]

def format_titles(titles):
    res = ""
    for title in titles[:5]:
        l = len(title)
        idx = 20
        while idx < l:
            res += title[idx - 20:idx] + "\n"
            idx += 20
        res += title[idx-20:] + "\n"
    print(res)
    return res


if __name__ == "__main__":
    topic = 0

    with open(THEME_DATA_FILE, "r") as f:
        data = json.load(f)
    dates = ["2020-" + date for date in data]

    tr_series = []
    cnt = 0
    for t in data['01-01'][topic]:
        if t[0] not in BLACK_LIST:
            tr_series.append(t[0])
            cnt += 1
        if cnt >= 10:
            break
    tr_data = []
    for date in data:
        cnt = 0
        idx = 0
        while cnt < 10:
            if data[date][topic][idx][0] not in BLACK_LIST:
                tr_data.append(["2020-" + date, data[date][topic][idx][1], data[date][topic][idx][0]])
                cnt += 1
            idx += 1
    
    wc_data = [("2020-" + date, []) for date in data]
    for idx in range(69):
        date = dates[idx][5:]
        for idy, term in enumerate(data[date][topic]):
            if term[0] not in BLACK_LIST:
                wc_data[idx][1].append(term)
    with open("news_top_title.json", "r") as f:
        top_titles = json.load(f)[topic]

    with open("news_emotion_count.json", "r") as f:
        news_ec = json.load(f)
    emotions = ["负面", "中性", "正面"]

    with open("cov_cnt.json", "r") as f:
        cc_data = json.load(f)


    theme_river = ThemeRiver(init_opts=opts.InitOpts(width="1200px", height="600px"))
    theme_river.add(
        series_name=tr_series,
        data=tr_data,
        label_opts=opts.LabelOpts(is_show=False),
        singleaxis_opts=opts.SingleAxisOpts(
            pos_top="50", pos_bottom="50", type_="time"
        ),
    )
    theme_river.set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
        legend_opts=opts.LegendOpts(pos_top="5%", is_show=True)
    )

    wc_tl = Timeline(init_opts=opts.InitOpts(width="1200px", height="600px"))
    idx = 0
    for date, tmp_data in wc_data:
        wc = WordCloud()
        wc.add(
            series_name="",
            data_pair=tmp_data
        )
        wc.set_global_opts(
            title_opts=opts.TitleOpts(title="词频统计", pos_top="top", pos_left="left"),
        )
        wc_tl.add(wc, date)
        idx += 1


    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="600px"))
    bar.add_xaxis(dates)
    for i in range(3):
        bar.add_yaxis(
            emotions[i],
            news_ec[topic][i],
            stack="stack1",
            category_gap="50%",
            label_opts=opts.LabelOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
            )
        )
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="情绪变化", pos_top="top", pos_left="center"),
        legend_opts=opts.LegendOpts(pos_top="5%", pos_left="center"),
    )

    line = Line(init_opts=opts.InitOpts(width="1200px", height="600px"))
    line.add_xaxis(dates)
    line.add_yaxis("确诊", cc_data[0], is_symbol_show=False)
    line.add_yaxis("死亡", cc_data[1], is_symbol_show=False)
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="疫情状况", pos_top="top", pos_left="center"),
        legend_opts=opts.LegendOpts(pos_top="5%", pos_left="center"),
    )


    tab = Tab()
    tab.add(chart=theme_river, tab_name="议题变化")
    tab.add(chart=bar, tab_name="情绪变化")
    tab.add(chart=line, tab_name="疫情状况")
    tab.add(chart=wc_tl, tab_name="词频统计")
    tab.render("index.html")


