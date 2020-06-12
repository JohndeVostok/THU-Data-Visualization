# Data Visualization - Homework 2

## Requirement

pyecharts: version > 1.0.0

``` shell
pip install pyecharts --user
```

## Start

prepare dataset

``` shell
mv imdb.csv hw2/.
cd hw2
python format.py
```

generate pie chart: pie.html

``` shell
python plot_pie.py
```

generate stacked histogram: hist.html

``` shell
python plot_hist.py
```

for more detail, please read REPORT.md