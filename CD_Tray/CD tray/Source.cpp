#include <Windows.h>
#include "resource.h"
#pragma comment(lib,"winmm.lib")

int main(){
	FreeConsole();
	mciSendString("set cdaudio door open",NULL,NULL,NULL);
}