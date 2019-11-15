#include "lib/MyMath.h"
#include <iostream>
using namespace std;

int main(){
	cout << isnegative(10) << endl;
	cout << ispositive(1) << endl;
	cout << perimeter_of_square(10) << endl;
	cout << square_of_numbers(10) << endl;
	cout << area_of_square(10) << endl;
	cout << to_abs(10) << endl;
	cout << to_abs(-10) << endl;
	cout << factorial(-1) << endl;
	cout << permutation(10, 3) << endl;
	cout << combination(10, 3) << endl;
	cout << exponent_of_number(11,5);
	system("pause"); //only for windows
	return 0;
}
