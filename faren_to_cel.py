import math
s = raw_input("put in some numbers here")
numbers = map(float, s.split())
i = int(raw_input("put in the iterations"))
while i > 0:
	first_num = numbers.pop(0)
	centi = ((first_num - 32) * 5)/9
	centi_fin = round(centi)
#	centi_fin2 = math.ceil(centi_fin)
	print int(centi_fin)
	i -= 1
