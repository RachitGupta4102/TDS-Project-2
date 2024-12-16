# Analysis Report for media.csv

## Dataset Overview

Shape: (2652, 8)

Columns: date, language, type, title, by, overall, quality, repeatability



             date language   type              title                 by      overall      quality  repeatability
count        2553     2652   2652               2652               2390  2652.000000  2652.000000    2652.000000
unique       2055       11      8               2312               1528          NaN          NaN            NaN
top     21-May-06  English  movie  Kanda Naal Mudhal  Kiefer Sutherland          NaN          NaN            NaN
freq            8     1306   2211                  9                 48          NaN          NaN            NaN
mean          NaN      NaN    NaN                NaN                NaN     3.047511     3.209276       1.494721
std           NaN      NaN    NaN                NaN                NaN     0.762180     0.796743       0.598289
min           NaN      NaN    NaN                NaN                NaN     1.000000     1.000000       1.000000
25%           NaN      NaN    NaN                NaN                NaN     3.000000     3.000000       1.000000
50%           NaN      NaN    NaN                NaN                NaN     3.000000     3.000000       1.000000
75%           NaN      NaN    NaN                NaN                NaN     3.000000     4.000000       2.000000
max           NaN      NaN    NaN                NaN                NaN     5.000000     5.000000       3.000000

## Null Value Analysis


date              99
language           0
type               0
title              0
by               262
overall            0
quality            0
repeatability      0
dtype: int64

## Key Insights

Highly correlated columns: quality  overall    0.825935
dtype: float64

Most common value in date: 21-May-06

Most common value in language: English

Most common value in type: movie

Most common value in title: Kanda Naal Mudhal

Most common value in by: Kiefer Sutherland

## Charts

![Correlation Heatmap][def]

![overall Distribution][def2]

![quality Distribution][def3]

![repeatability Distribution](repeatability_distribution.png)

![date Bar Plot](date_barplot.png)

![language Bar Plot](language_barplot.png)

![type Bar Plot](type_barplot.png)

![title Bar Plot](title_barplot.png)

![by Bar Plot](by_barplot.png)


[def]: correlation_heatmap.png
[def2]: overall_distribution.png
[def3]: quality_distribution.png