#include <iostream>
using namespace std;
int main(){
int len;
string text;
cout << "Please enter a text:" << endl;
cin >> text;
len = text.size();
while (-1 < len){
cout << text[len];
len--;
}
cout << endl;
return 1;
}
