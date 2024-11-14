import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm

df = pd.read_csv('data/plant_ref.csv')

df = df.drop(['시도명','시군구명','상세주소'], axis=1)
df = df.rename(columns={'분포식물국명': 'name'})

df.to_csv('./data/plant_ref2.csv', index=False)


