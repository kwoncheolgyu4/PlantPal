import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm

df = pd.read_csv('./data/plant.csv')

df['addr'] = df['시도명'] + ' ' + df['시군구명'] + ' ' + df['상세주소']
df = df.drop(['분포식물학명'], axis=1)

df.to_csv('plant_ref.csv', index=False)


