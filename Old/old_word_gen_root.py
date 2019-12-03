import random as r
import sys

# Consonante inicial no puede omitirse
c_   = ['','','p','t','k','m','n','f','s','x','l']
# Consonante intermedia simepre tiene que existir
c    = ['p','t','k','m','n','f','s','x','l']
# Consonante final no puede ser oclusiva y puede omitirse
co_  = ['','','m','n','f','s','x','l']

# Vocal inicial simple y no puede ser schwa
v    = ['a','e','i','o','u']

# Vocal intermedia o final puede ser simple o compuesta de un aproximante (segun reglas)
# nunca abierta simple, ni terminar en una
vva_ = ['e','i','o','u','a',
		'e','i','o','u','a',
		'ae','ai','ao','au',
		'iu','ie','ui','uo',
		'ei','eu','eo',
		'oi','ou','oe']

if __name__ == "__main__":
	if len(sys.argv) > 1:
		n = int(sys.argv[1])
	else:
		n = 36

	arr = []
	for i in range(n*7):
		last = r.choice(c_)+r.choice(v)+r.choice(c)+r.choice(vva_)+r.choice(c)+r.choice(vva_)+r.choice(co_)

		last += "   " if len(last)<8 else ""

		arr.append(last)

		if len(arr)==7:
			print "%s	%s	%s	%s	%s	%s	%s" % tuple(arr)
			arr = []
