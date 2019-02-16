import pandas as pd

# https://stackoverflow.com/questions/26577516/how-to-test-if-a-string-contains-one-of-the-substrings-in-a-list
# https://on-your-mark.tokyo/tips/python/contains/

df = pd.read_csv("data.csv")
# client_id と日付の昇順でソート
df = df.sort_values(by=["EVENT_TIME"], ascending=True)
# データ件数が多く後続の計算に時間を擁するのでデータを減らす
df = df[1:3000]

# 直前のいくつのデータを取得するか

NAME_LIST = ['CPU','UI','MEM']


df = df[df['ALARM_KIND'].str.contains('|'.join(NAME_LIST))]

df['TAG'] = 'UNKNOWN'

for v in NAME_LIST:
    df.loc[df['ALARM_KIND'].str.contains(v), 'TAG'] = v
print(df)
