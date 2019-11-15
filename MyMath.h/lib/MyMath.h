// #include <stdbool.h> //for c compability

#define Pi 3.14;

bool isnegative(float number){
	if (number > 0){
		return false;
	}
	else{
		return true;
	}
}

bool ispositive(float number){
	if (number < 0){
		return false;
	}
	else
	{
		return true;
	}
}

int perimeter_of_square(int number){
	return number * 4;
}

int area_of_square(int number){
	return number * number;
}

int square_of_numbers(int number){
	return number * number;
}

double to_abs(int number){
	if (number > 0){
		return number;
	}
	else
	{
		return number * -1;
	}
}

int factorial(int number){
	if (number < 0)
	{
		return false;
	}
	else
	{
		int result = 1;
		for (int i = 1; i <= number; i++){
			result *= i;

		}
		return result;
	}
	
}


int permutation(int n, int r){
	return factorial(n) / factorial(n - r);
}

int combination(int n, int r){
	return factorial(n) / (factorial(n - r) * factorial(r));
}

int exponent_of_number(int number,int base){
	int result = 1;
	for (int i = 1; i <= base;i++){
		result *= number;
	}
	return result;
}