#include <iostream>//input-output stream
#include <string>//strings: "Hello world"
#include <fstream>//file stream (for file operation)
#include <Windows.h>//special windows library. only used once in the code. not really even necessary.
using namespace std;
//all of the functions
void encrypter();
void decoder();
//special function to write a character to a file
void writeFile(char fileInput);
//main code (Not really, it's mostly in the functions)
int main() {
	system("color a");//DA MATRIX COLORS, a command specifically for windows
	/////////////////////////////////////////////////////////////
	int encodeDecode;//integer value to determine the program to be run, the encrypter, or decoder
	cout << "Welcome to my cipher program!\nRun the Encrypter program or Decoder program?\n 1 - Encrypter program\n 2 - Decoder program";
	bool validEntry = false;
	while (!validEntry) {//while loop waits until a valid entry is recieved, in this case, either 1 or 2
		cout << "\n>>> ";
		cin >> encodeDecode;//user inputs the value for the int
		if (encodeDecode == 1) {
			validEntry = true;//if its 1, then it is a valid entry
		}
		else if (encodeDecode == 2) {
			validEntry = true;//same if its 2
		}
		else {
			cout << "ERROR: Entry not valid, try again";//if not, alert the user, and the loop runs again
		}
	}
	system("cls");//clear the screen, because, why not?
	/////////////////////////////////////////////////////////////
	if (encodeDecode == 1) {
		encrypter();//if the previous int was 1, run the encrypter
	}
	else {
		decoder();//if it was 2, run the decoder
	}
	/////////////////////////////////////////////////////////////
}
//the function for the encrypter program
void encrypter() {
	//the following section is simply just to open the file and close it again, allowing it to refresh the data from the last time:
	/////////////////////////////////////////////////////////////
	ofstream file1;
	file1.open("encryptedMessage.txt", ios::trunc);
	file1.close();
	/////////////////////////////////////////////////////////////
	string msg;//the message to be encrypted
	string key;//the key to encrypt it with
	cout << "Enter the message to encrypt:";
	cout << "\n>>> ";
	cin.ignore();
	getline(cin, msg);//console input, the "getline()" function is specially for strings
	cout << "\n(";
	cout << msg.length();//print the length of the message to let the user know
	cout << " characters long)";
	cout << "\nOk. Enter the key for encryption. KEEP IT. \nThis is necessary for decoding, and must be the same character length as the message\n";
	/////////////////////////////////////////////////////////////
	for (int i = 0;i < msg.length();i++){
		cout << " ";
	}
	cout << "    |END";
	/////////////////////////////////////////////////////////////
	bool validEntry = false;
	while (!validEntry) {//more valid entry stuff. the loop is to get a console input from the user to be the key, which has to be the same length as the message
		cout << "\n>>> ";
		cin.ignore();
		getline(cin, key);//more getline();
		if (msg.length() - 1 <= key.length()) {//this part is kind of weird... it should be if (msg.length() <= key.length()), but it only works with the -1 after msg.length() IDK WHY THERE IS NO REASON FOR IT TO BE LIKE THIS
			validEntry = true;
		}
		else {
			cout << "ERROR: Entry not valid, try again";//"ERROR ERROR ERROR ERROR...."
		}
	}
	/////////////////////////////////////////////////////////////
	cout << "_________________________________________________\n\nThe encrypted message is: \n(This will also appear in a .txt file in the same folder as the application, along with the char loop ID)\n";
	int loopList[10000] = { msg.length(),0 };//makes a list of integers in order to keep track of how many times the characters will loop over when encoded
	for (int loop = 0; loop < msg.length(); loop++) {//repeat this msg.length() times, so you get a character that is encoded for each of the characters in the original message
		int val1 = (int)msg[loop];//the ascii code of the specified number character in the message
		int val2 = (int)key[loop];//the ascii code for the corresponding character in the key
		int valEncoded = (val1 + val2);//the encoded value, just the ascii codes of the message and key
		int loops = 0;
		for (int i = 1; i <= 3; i++) {
			if (valEncoded > 126) {//if the encoded value exceeds 126, the last char I use, then loop back to the beginning (there are 94 characters in all)
				valEncoded -= 94;
				loops = i;//add one to the number of times looped
			}
		}
		loopList[loop] = loops;//add the loop number of this character to the list
		char loopChar = valEncoded;//make a character from the encoded value
		cout << loopChar;//print it
		writeFile(loopChar);//save it to the file
		loopChar = ' ';//refresh the character
	}
	cout << "\n\nThe character loop ID is: (This is also necessary when decoding the message)\n";
	for (int i = 0; i < msg.length(); i++) {//when done, print the loops of each character. this appears on new lines for easier decoding
		cout << loopList[i] << "\n";
		char loopChar2 = '0' + loopList[i];
		writeFile('\n');
		writeFile(loopChar2);
	}
	writeFile('\n');
	cout << "\n\nWhen Decoding the message, you will NEED the char loop ID code and the key to find what it is.\nWhen you send the message, send it with the char loop ID as well, but make sure\nyour correspondent has the key to the message.";
	while (1 == 1) {}//random loop to keep the program running forever and ever and ever! (without doing anything, until closed)
	/////////////////////////////////////////////////////////////
}
//the one for the decoder
void decoder() {
	string key;
	string msgCode;
	cout << "Enter the encrypted message:\n";
	cout << ">>> ";
	cin.ignore();
	getline(cin, msgCode);
	cout << "\n(";
	cout << msgCode.length();
	cout << " characters long)";
	cout << "\nOk. Enter the char code ID (One by one), which should only be in 0s, 1s, and 2s:";
	int loopList[10000] = { msgCode.length(),0 };
	for (int i = 0; i < msgCode.length(); i++) {
		cout << "\n>>> ";
		cin >> loopList[i];
	}
	cout << "\nOk. Enter the key that was used for encryption \nThis must be the same character length as the message:\n";
	/////////////////////////////////////////////////////////////
	for (int i = 0;i < msgCode.length();i++){
		cout << " ";
	}
	cout << "    |END";
	/////////////////////////////////////////////////////////////
	bool validEntry = false;
	while (!validEntry) {
		cout << "\n>>> ";
		cin.ignore();
		getline(cin, key);
		if (msgCode.length() - 1 <= key.length()) {
			validEntry = true;
		}
		else {
			cout << "ERROR: Entry not valid, try again";
		}
	}
	system("cls");
	/////////////////////////////////////////////////////////////
	cout << "_________________________________________________\n\nThe message is:\n";
	for (int loop = 0; loop < msgCode.length(); loop++) {
		int val1 = (int)msgCode[loop];
		int val2 = (int)key[loop];
		int valDecoded;
		if (loopList[loop] == 1) {
			int valDecoded = val1 - val2 + 94;
			char loopChar = valDecoded;
			cout << loopChar;
		}
		else if (loopList[loop] == 2) {
			int valDecoded = val1 - val2 + 94 + 94;
			char loopChar = valDecoded;
			cout << loopChar;
		}
		else {
			int valDecoded = val1 - val2;
			char loopChar = valDecoded;
			cout << loopChar;
		}
	}
	while (1 == 1) {}
	/////////////////////////////////////////////////////////////
}
//the file stream function
void writeFile(char fileInput) {
	ofstream file;
	file.open("encryptedMessage.txt", ios::out | ios::app);
	file << fileInput;
	file.close();
}
