# Amaan Muhammad
# PSID: 1607608

integers = input().split()

non_neg_int = []

for num in integers:
    num = int(num)
    if num >= 0:
        non_neg_int.append(num)

non_neg_int.sort()

for i in non_neg_int:
    print(i, end=' ')
