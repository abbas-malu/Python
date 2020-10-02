import pandas as pd 

reviews_path = 'winemag-data-130k-v2.csv/winemag-data-130k-v2.csv'
reviews = pd.read_csv(reviews_path)
# pd.set_option('display.max_rows', 500)
# print(reviews.describe())
# print(reviews.head())
ser = pd.Series(reviews.loc[(reviews.description.str.contains('tropical')) & (reviews.points>=1),'points'])
# print(ser)

def points_increase(row):
    row.points += 1
    return row

point_inc = reviews.apply(points_increase,axis='columns')
print(point_inc.loc[:,'points'])