def perm(one,two):
	two = one - two
	toplam = 1
	for i in range(one,two,-1):
		toplam *= i
	return toplam
