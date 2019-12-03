import random as r
import sys
import codecs

# Consonante inicial no puede omitirse
c_ = [u'', u'', unichr(273), unichr(946), u'x', u'm', u'n', u'f', u's', u'l']
# Consonante intermedia simepre tiene que existir
c = [unichr(273), unichr(946), u'x', u'm', u'n', u'f', u's', u'l']

# Vocal inicial simple y no puede ser schwa
v = [u'a', u'e', u'i', u'o', u'u']
# Vocal puede ser simple o compuesta de un aproximante (segun reglas)
vva_ = [u'a', u'e', u'i', u'o', u'u', u'a', u'e', u'i', u'o', u'u',
		u'ae', u'ai', u'ao', u'au', u'ei', u'eu', u'oi', u'ou',
		u'eo', u'oe', u'ie', u'uo', u'iu', u'ui']

if __name__ == "__main__":
	if len(sys.argv) > 1:
		n = int(sys.argv[1])
	else:
		n = 100

	arr = []
	for i in range(n):
		first = r.choice(c_)+r.choice(vva_)+r.choice(c_)
		secon = r.choice(c_)+r.choice(vva_)+r.choice(c_)
		third = r.choice(c_)+r.choice(vva_)+r.choice(c_)

		fs = u' l ' if (first[-1] in v and secon[0] in v) else u' '
		st = u' l ' if (secon[-1] in v and third[0] in v) else u' '

		arr.append(first+fs+secon+st+third)

		first = r.choice(c_)+r.choice(vva_)+r.choice(c_)
		secon = r.choice(c_)+r.choice(vva_)+r.choice(c_)

		fs = u' l ' if (first[-1] in v and secon[0] in v) else u' '

		arr.append(first+fs+secon)

	with codecs.open("new_word_list.txt", "a+", encoding="utf-8") as f:
		for w in arr:
			f.write(w+"\n")
