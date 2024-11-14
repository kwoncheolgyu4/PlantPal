import pandas as pd
from tqdm import tqdm
from geopy.geocoders import Nominatim

# CSV 파일 읽기
df = pd.read_csv('./data/plant_select_all.csv')

# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo_local = Nominatim(user_agent='South Korea')  # 지역 설정
        location = geo_local.geocode(address)
        geo = [location.latitude, location.longitude]
        return geo
    except:
        return [0, 0]

# tqdm을 사용하여 주소 목록을 순회하며 위도와 경도 추가
for idx, addr in enumerate(tqdm(df.addr)):
    df.loc[idx, 'latitude'] = geocoding(addr)[0]
    df.loc[idx, 'longitude'] = geocoding(addr)[1]

# 위도와 경도가 추가된 데이터프레임을 새로운 CSV 파일로 저장
df.to_csv('./data/plant_select_with.csv', index=False, encoding='utf-8-sig')
