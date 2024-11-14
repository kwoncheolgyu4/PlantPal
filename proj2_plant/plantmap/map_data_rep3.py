import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm

df = pd.read_csv('./data/plant_select_with.csv')

df = df[df['latitude'] != 0.0]

df.to_csv('./data/plant_select_with_ref.csv', index=False, encoding='utf-8-sig')


