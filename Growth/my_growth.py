import pandas as pd

#dfの現在のidxの直前からdelta前までのdfを取得
def get_before_df(df,idx,delta):
    before_df = df.ix[idx-delta:idx-1]
    return before_df

#アイテムを配列として取得
def get_items(df,item_name):
    strs = []
    for idx in df.index:
        #行の取得
        elems = df.ix[idx]
        strs.extend((elems[item_name] + ",").rstrip(',').split(','))
        # before_df = get_before_df(df,idx,delta)
        # strs = get_items(before_df,'ALARM_KIND')
    return strs
        # prinefore_df)



df = pd.read_csv("my_data.csv")
# client_id と日付の昇順でソート
df = df.sort_values(by=["EVENT_TIME"], ascending=True)
# データ件数が多く後続の計算に時間を擁するのでデータを減らす
df = df[1:3000]

# 直前のいくつのデータを取得するか
delta = 2

transactions = []
strs = []
previous_client_id = ""

for idx in df.index:
    # 行の取得
    elems = df.ix[idx]
    if elems["ERROR"] and (idx - delta) > -1:
        before_df = get_before_df(df,idx,delta)
        strs = get_items(before_df,'ALARM_KIND')
        transactions.append(strs)

        

# print(transactions)
        # 直前3のデータを取得


'''
KW: python pandas 時間の間
http://sinhrks.hatenablog.com/entry/2015/05/18/233505

idxがDatetimeの場合
df['2015-05-17']
とするとその日にちのデータ全てを取得できる

'''
import pyfpgrowth
#3,0.7
patterns = pyfpgrowth.find_frequent_patterns(transactions, 0)
rules = pyfpgrowth.generate_association_rules(patterns, 0.0)

print(patterns)
print(rules)
#     client_id = elems["ALARM_NAME"]


#     check_error = elms[""]
#     if(previous_client_id != ""):
#         if (previous_client_id != client_id):
#             transactions.append(strs)
#             strs = []
#             strs.extend(((elems["second"] + ",") * elems["third"]).rstrip(',').split(','))
#         else:
#             strs.extend(((elems["second"] + ",") * elems["third"]).rstrip(',').split(','))
#     else:
#         strs.extend(((elems["second"] + ",") * elems["third"]).rstrip(',').split(','))
#     previous_client_id = client_id
# if strs:
#     transactions.append(strs)

print(transactions)