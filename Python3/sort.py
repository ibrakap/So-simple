from os import system

def listtolower(*args):
	list = []
	for i in args:
		list.append(i)
	list.sort()
	return list

	
print(listtolower(1,3,5,7,9))
print(listtolower(9,10,5,7,3))
		
system("pause")