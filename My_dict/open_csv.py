import csv

data1 = 'dict.csv'

with open(data1, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばす場合

    for row in reader:
        print(row)