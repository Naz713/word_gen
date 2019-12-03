import csv
from itertools import groupby

arr = set()
with open("word_list.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    for line in csv_reader:
        arr.add(line[0])

arr = list(arr)
arr.sort()
print len(arr)

with open('word_list.csv', mode='w+') as f:
    writer = csv.writer(f, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for x in arr:
        writer.writerow([x])

with open('sufix_word_list.csv', mode='w+') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for k, x in groupby(arr, lambda y: y[:2] if len(y) > 1 else y[0]):
        writer.writerow(list(x))

    writer.writerow(['/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /'])

    arr.sort(key=lambda y: "".join(reversed(y)))
    for k, x in groupby(arr, lambda y: y[-2:] if len(y) > 1 else y[0]):
        writer.writerow(list(x))
