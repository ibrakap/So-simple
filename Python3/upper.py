upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

text = "DenemeYazisi"

def doupper(text):
	temp=""
	for i in text:
		for a in range(len(lower)):
			if i == lower[a]:
				temp += upper[a]

		else:
			for f in range(len(upper)):
				if i == upper[f]:
					temp += upper[f]
	return temp
def dolower(text):
	temp=""
	for i in text:
                for a in range(len(lower)):
                        if i == lower[a]:
                        	temp += lower[a]
                else:
                        for f in range(len(upper)):
                                if i == upper[f]:
                                	temp += lower[f]
	return temp

print(dolower(text))
print(doupper(text))
