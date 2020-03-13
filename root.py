import csv
from itertools import groupby


def agrupator(word, length, prefix=True):
    sufix = ''
    counter = length
    if not prefix:
        word = "".join(reversed(word))
    for letter in word:
        sufix += letter
        if letter not in ['\xce', '\xc4', '\x91', '\xb2']:
            counter -= 1
        if counter == 0:
            return sufix if prefix else "".join(reversed(sufix))
    return sufix if prefix else "".join(reversed(sufix))


# tomamos la lista de palabras creadas separadas por silabas con espacios, una palabra por renglon
arr = set()
with open("old_word_list.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    for line in csv_reader:
        arr.add(line[0])

# quitamos repetidos
arr = list(arr)
# ordenamos
arr.sort()
print len(arr)

# guardamos en un archivo
with open('sorted_word_list.csv', mode='w+') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for x in arr:
        writer.writerow([x])

length = 3

'''
Guardamos las palabras acomodadas por como comienzan y terminan
comparten sufijos y prefijos
'''

with open('sufix_word_list.csv', mode='w+') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for k, x in groupby(arr, lambda y: agrupator(y, length)):
        writer.writerow(list(x))

    writer.writerow(['/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /'])

    arr.sort(key=lambda y: "".join(reversed(y)))
    for k, x in groupby(arr, lambda y: agrupator(y, length, False)):
        writer.writerow(list(x))

length = 2

# separamos las palabras y hacemos una lista de silabas
arr_root = reduce(lambda z, y: y.split(" ") + z, arr, [])
# quitamos repetidos
arr = set(arr_root)
arr = list(arr)
# ordenamos
arr.sort()

'''
Guardamos la lista de raices/silabas con relaciones entre unas o otras, que empiezan o terminan igual
'''
with open('flex_root_list.csv', mode='w+') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for k, x in groupby(arr, lambda y: agrupator(y, length)):
        writer.writerow(list(x))

    writer.writerow(['/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /'])

    arr.sort(key=lambda y: "".join(reversed(y)))
    for k, x in groupby(arr, lambda y: agrupator(y, length, False)):
        writer.writerow(list(x))


