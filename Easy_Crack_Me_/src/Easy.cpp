#include <iostream>
using namespace std;

int main(){
	string pass;
	cout << "Enter Password:" << endl;
	cin >> pass;
	if (pass == "0x86"){
		cout << "Your password true";
	}
	else{
		cout << "False,try again" << endl;
	}
	return 0;
}
