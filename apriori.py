from akapriori import apriori

transactions = [
    ("apricot", "apple", "cherry", "plum", "banana"),
    ("strawberry", "plum", "cherry"),
    ("persimmon", "peach", "banana", "apple"),
    ("kiwi fruit", "apple", "pear"),
    ("cherry", "pear", "banana"),
    ("watermelon", "apple"),
    ("plum", "banana"),
    ("pear", "peach", "cherry", "banana", "apricot"),
    ("pineapple", "apple", "plum"),
    ("banana", "plum", "peach"),
    ("grape", "cherry"),
    ("mandarin", "plum"),
    ("melon", "apple", "persimmon", "plum"),
    ("peach", "cherry", "apple"),
    ("apple", "mandarin", "plum", "persimmon"),
]

rules = apriori(transactions, support=0.05, confidence=0.3, lift=2)
rules_sorted = sorted(rules, key=lambda x: (x[4], x[3], x[2]), reverse=True) # ORDER BY lift DESC, confidence DESC, support DESC

for r in rules_sorted:
    print(r)