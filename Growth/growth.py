import pandas as pd
df = pd.read_csv("data.csv")
# client_id と日付の昇順でソート
df = df.sort_values(by=["KIND"], ascending=True)
# データ件数が多く後続の計算に時間を擁するのでデータを減らす
df = df[1:3000]

transactions = []
strs = []
previous_client_id = ""
for idx in df.index:
    elems = df.ix[idx]
    client_id = elems["KIND"]
    if(previous_client_id != ""):
        if (previous_client_id != client_id):
            transactions.append(strs)
            strs = []
            strs.extend(((elems["second"] + ",") * elems["third"]).rstrip(',').split(','))
        else:
            strs.extend(((elems["second"] + ",") * elems["third"]).rstrip(',').split(','))
    else:
        strs.extend(((elems["second"] + ",") * elems["third"]).rstrip(',').split(','))
    previous_client_id = client_id
if strs:
    transactions.append(strs)

print(transactions)