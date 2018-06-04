#include <iostream>
#include <windows.h>

using namespace std;

void KeyPress(char key){
	INPUT ip;
 
	// Set up a generic keyboard event.
	ip.type = INPUT_KEYBOARD;
	ip.ki.wScan = 0; // hardware scan code for key
	ip.ki.time = 0;
	ip.ki.dwExtraInfo = 0;
	
	// Press the "A" key
	ip.ki.wVk = key; // virtual-key code for the key
	ip.ki.dwFlags = 0; // 0 for key press
	SendInput(1, &ip, sizeof(INPUT));
	
	// Release the key
	ip.ki.dwFlags = KEYEVENTF_KEYUP; // KEYEVENTF_KEYUP for key release
	SendInput(1, &ip, sizeof(INPUT));
}

int main(){
	ShowWindow(GetConsoleWindow(),SW_HIDE);
	int loop = 1;
	bool pressed=false;
	while(loop==1){
		if(GetKeyState(0x45)&0x800){    //E key to S
			KeyPress(VK_BACK);
			KeyPress(0x53);
			pressed=true;
			while(pressed==true){
				if(GetAsyncKeyState(0x45)&0x8000){
					Sleep(1);
				}else{
					pressed=false;   //Make it so that when it is pressed, it doesn't span endless ENTER keys for the keylogs, it has to wait until the key is released
				}
			}
		}
		if(GetKeyState(0x53)&0x800){    //S key to E
			KeyPress(VK_BACK);
			KeyPress(0x45);
			pressed=true;
			while(pressed==true){
				if(GetAsyncKeyState(0x53)&0x8000){
					Sleep(1);
				}else{
					pressed=false;   //Make it so that when it is pressed, it doesn't span endless ENTER keys for the keylogs, it has to wait until the key is released
				}
			}
		}
	}
 }
