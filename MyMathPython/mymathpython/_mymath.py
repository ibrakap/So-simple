def isnegative(number):
	if number < 0:
	   return True
	else:
		return False

def ispositive(number):
	if number > 0:
	   return True
	else:
	   return False

def to_abs(number):
    if number >= 0:
        return number
    else:
        return number * -1

def square_of_number(number):
		return number * number

def perimeter_of_square(number):
    return number * 4

def area_of_square(number):
	return number * number

def factorial(number):
    if number < 0:
        return False
    else:
        result = 1
        for i in range(1,number+1):
            result *= i
        return result
def permutation(n,r):
    return factorial(n) / factorial(n - r)

def combination(n, r):
	return factorial(n) / (factorial(n - r) * factorial(r))

def exponent_of_number(number,base):
    result = 1
    for i in range(1,base+1):
        result *= number
    return result
