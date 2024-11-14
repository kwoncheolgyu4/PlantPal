import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('./data/plant_select_with_ref.csv')

# JavaScript 형식으로 문자열 생성
positions_js = "const positions = [\n"
for _, row in df.iterrows():
    positions_js += f"    {{\n        content: '<div>{row['name']}</div>',\n"
    positions_js += f"        latlng: new kakao.maps.LatLng({row['latitude']}, {row['longitude']})\n    }},\n"
positions_js = positions_js.rstrip(",\n") + "\n];"

# JavaScript 파일로 저장
with open('./data/positions.js', 'w', encoding='utf-8') as f:
    f.write(positions_js)