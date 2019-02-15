from akapriori import apriori
import csv
from akapriori import apriori

# csv_file = open("./yoko.csv", "r", encoding="utf8", errors="", newline="")
csv_file = open("./tate.csv", "r", encoding="utf8", errors="", newline="")

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)


transactions = []
# print(header)
for row in f:
    transactions.extend(row)

# transactions2 =[]
transactions = [tuple(transactions)]
print(transactions)

# transactions_cpy = transactions.copy()

# transactions.append('apple')

# for i in range(10):
#     for v in transactions_cpy:
#         transactions.append(v)

rules = apriori(transactions, support=0.05, confidence=0.3, lift=2)
rules_sorted = sorted(rules, key=lambda x: (x[4], x[3], x[2]), reverse=True) # ORDER BY lift DESC, confidence DESC, support DESC

for r in rules_sorted:
    print(r)
