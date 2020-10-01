import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import json

netflix_data = pd.read_csv('archive/netflix_titles.csv')
# print(netflix_data.columns)
# print(netflix_data.loc[11:120,'title'])
# print(netflix_data.release_year == 2018)
# print(netflix_data.loc[netflix_data.release_year == 2018].head())
for year in netflix_data.release_year:
    # print(year.unique())
    pass
# print(len(list(range(len(netflix_data.title),0,-1))))
years = netflix_data.release_year.value_counts()
print(years)