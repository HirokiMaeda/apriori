from akapriori import apriori
import csv
from akapriori import apriori

csv_file = open("./yoko.csv", "r", encoding="utf8", errors="", newline="")
#リスト形式
# f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

# header = next(f)

transactions = []
# print(header)
for row in f:
    transactions.append(tuple(row))

print(transactions)

rules = apriori(transactions, support=0.05, confidence=0.3, lift=2)
rules_sorted = sorted(rules, key=lambda x: (x[4], x[3], x[2]), reverse=True) # ORDER BY lift DESC, confidence DESC, support DESC

for r in rules_sorted:
    print(r)

# transactions = [ tuple(row) for row in f]

# transactions =[[tuple(row)] for row in f]
