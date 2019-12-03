import csv
import random as r
import sys

v = ['a','e','i','o','u']
co = ['m','n','f','s','x','l']

if __name__ == "__main__":
	arr = []
	with open("word_list.csv") as f:
		csv_reader = csv.reader(f, delimiter=' ')
		for line in csv_reader:
			arr.append(line[0])

	print "%s roots" % len(arr)

	if len(sys.argv) > 1:
		n = int(sys.argv[1])
	else:
		n = 35

	for i in range(n):
		first = r.choice(arr)
		second = r.choice(arr)
		# third = r.choice(arr)
		# fourth = r.choice(arr)
		# fifth = r.choice(arr)

		fs = "'" if first[-1] in v and second[0] in v else ""
		# st = r.choice(co) if second[-1] in v and third[0] in v else ""
		# tf = r.choice(co) if third[-1] in v and fourth[0] in v else ""
		# ff = r.choice(co) if third[-1] in v and fourth[0] in v else ""

		print first + fs + second # + st + third + tf + fourth + ff + fifth
