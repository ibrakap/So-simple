url = input("\033[1;32mEnter an adres:")
number = int(input("Enter a value:"))
number += 1

for i in range(0,number):
    print("\033[1;32m{} sending ddos: {}".format(url,i))
