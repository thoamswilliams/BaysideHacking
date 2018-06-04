#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void keySense(int keyCode){
	if (GetAsyncKeyState(VK_LBUTTON)&&0X800){
		cout<<"up";
	}
}

int main(){
	while(1==1){
		keySense();
	}
}
