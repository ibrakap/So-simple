#!/usr/bin/python3
def GetBase(number,base):
	result = 1
	base +=1
	for i in range(1,base):
		result *= number
	print(result)

sayı = int(input("Sayı girin:"))
üs = int(input("Üs ü girin:"))
GetBase(sayı,üs)
