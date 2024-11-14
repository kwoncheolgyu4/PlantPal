import pandas as pd


df = pd.read_csv('data/plant_ref2.csv')

df_selected = df[df['name'].isin(['가시오갈피','곰취','꿀풀','넉줄고사리','담배풀','메밀','봉선화','참취','아욱','제비쑥'])]

df_selected.to_csv('./data/plant_select_all.csv', index=False, encoding='utf-8-sig')


