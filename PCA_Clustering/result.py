import csv

# 对分3簇的进行整合
res = [[13, 14, 17, 29, 30, 38, 47, 48, 51, 67, 68, 77, 78, 88, 98, 99, 106, 118], [],
       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 19, 20, 21,
        22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 49, 50, 52, 53, 54, 55,
        56, 57, 58, 59, 60, 61, 62, 63, 64,
        65, 66, 69, 70, 71, 72, 73, 74, 75, 76, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97,
        100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123,
        124]]

first = []
second = []

with open("meituan.csv", encoding='utf8') as f:
    reader = csv.reader(f)
    header = next(reader)
    i = 0
    for row in reader:
        if i in res[0]:
            first.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
        else:
            second.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
        i += 1
