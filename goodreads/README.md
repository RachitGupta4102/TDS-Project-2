# Analysis Report for goodreads.csv

## Dataset Overview

Shape: (10000, 23)

Columns: book_id, goodreads_book_id, best_book_id, work_id, books_count, isbn, isbn13, authors, original_publication_year, original_title, title, language_code, average_rating, ratings_count, work_ratings_count, work_text_reviews_count, ratings_1, ratings_2, ratings_3, ratings_4, ratings_5, image_url, small_image_url



            book_id  goodreads_book_id  ...                                          image_url                                    small_image_url
count   10000.00000       1.000000e+04  ...                                              10000                                              10000
unique          NaN                NaN  ...                                               6669                                               6669
top             NaN                NaN  ...  https://s.gr-assets.com/assets/nophoto/book/11...  https://s.gr-assets.com/assets/nophoto/book/50...
freq            NaN                NaN  ...                                               3332                                               3332
mean     5000.50000       5.264697e+06  ...                                                NaN                                                NaN
std      2886.89568       7.575462e+06  ...                                                NaN                                                NaN
min         1.00000       1.000000e+00  ...                                                NaN                                                NaN
25%      2500.75000       4.627575e+04  ...                                                NaN                                                NaN
50%      5000.50000       3.949655e+05  ...                                                NaN                                                NaN
75%      7500.25000       9.382225e+06  ...                                                NaN                                                NaN
max     10000.00000       3.328864e+07  ...                                                NaN                                                NaN

[11 rows x 23 columns]

## Null Value Analysis


book_id                         0
goodreads_book_id               0
best_book_id                    0
work_id                         0
books_count                     0
isbn                          700
isbn13                        585
authors                         0
original_publication_year      21
original_title                585
title                           0
language_code                1084
average_rating                  0
ratings_count                   0
work_ratings_count              0
work_text_reviews_count         0
ratings_1                       0
ratings_2                       0
ratings_3                       0
ratings_4                       0
ratings_5                       0
image_url                       0
small_image_url                 0
dtype: int64

## Key Insights

Highly correlated columns: ratings_count            work_ratings_count         0.995068
ratings_4                work_ratings_count         0.987764
ratings_count            ratings_4                  0.978869
goodreads_book_id        best_book_id               0.966620
ratings_5                work_ratings_count         0.966587
ratings_count            ratings_5                  0.964046
ratings_3                ratings_4                  0.952998
                         ratings_2                  0.949596
                         work_ratings_count         0.941182
ratings_count            ratings_3                  0.935193
ratings_4                ratings_5                  0.933785
work_id                  goodreads_book_id          0.929356
ratings_2                ratings_1                  0.926140
work_id                  best_book_id               0.899258
work_ratings_count       ratings_2                  0.848581
ratings_2                ratings_count              0.845949
ratings_4                ratings_2                  0.838298
ratings_3                ratings_5                  0.825550
work_text_reviews_count  ratings_4                  0.817826
                         work_ratings_count         0.807009
ratings_3                ratings_1                  0.795364
work_text_reviews_count  ratings_count              0.779635
                         ratings_5                  0.764940
ratings_3                work_text_reviews_count    0.762214
ratings_1                ratings_count              0.723144
                         work_ratings_count         0.718718
ratings_2                ratings_5                  0.705747
dtype: float64

Most common value in isbn: 375700455

Most common value in authors: Stephen King

Most common value in original_title:  

Most common value in title: Selected Poems

Most common value in language_code: eng

Most common value in image_url: https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png

Most common value in small_image_url: https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png

## Charts

![Correlation Heatmap][def]

![book_id Distribution][def2]

![goodreads_book_id Distribution][def3]

![best_book_id Distribution](best_book_id_distribution.png)

![work_id Distribution](work_id_distribution.png)

![books_count Distribution](books_count_distribution.png)

![isbn13 Distribution](isbn13_distribution.png)

![original_publication_year Distribution](original_publication_year_distribution.png)

![average_rating Distribution](average_rating_distribution.png)

![ratings_count Distribution](ratings_count_distribution.png)

![work_ratings_count Distribution](work_ratings_count_distribution.png)

![work_text_reviews_count Distribution](work_text_reviews_count_distribution.png)

![ratings_1 Distribution](ratings_1_distribution.png)

![ratings_2 Distribution](ratings_2_distribution.png)

![ratings_3 Distribution](ratings_3_distribution.png)

![ratings_4 Distribution](ratings_4_distribution.png)

![ratings_5 Distribution](ratings_5_distribution.png)

![isbn Bar Plot](isbn_barplot.png)

![authors Bar Plot](authors_barplot.png)

![original_title Bar Plot](original_title_barplot.png)

![title Bar Plot](title_barplot.png)

![language_code Bar Plot](language_code_barplot.png)

![image_url Bar Plot](image_url_barplot.png)

![small_image_url Bar Plot](small_image_url_barplot.png)


[def]: correlation_heatmap.png
[def2]: book_id_distribution.png
[def3]: goodreads_book_id_distribution.png