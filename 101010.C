#include <stdio.h>
#include<conio.h>
#define LED_ADDRESS 0xFF00
unsigned char memory[6553];
void writeMemory(unsigned short address, unsigned char data)
{
memory[address] = data;
if (address == LED_ADDRESS)
{
if (data == 1)
printf("LED Status : ON\n");
else
printf("LED Status : OFF\n");
}
}
unsigned char readMemory(unsigned short address)
{
return memory[address];
}
int main()
{
clrscr();
printf("Memory-Mapped I/O Simulation\n\n");
printf("Writing 1 to address 0x%X\n", LED_ADDRESS);
writeMemory(LED_ADDRESS, 1);
printf("\nWriting 0 to address 0x%X\n", LED_ADDRESS);
writeMemory(LED_ADDRESS, 0);
printf("\nWriting 1 to address 0x%X\n", LED_ADDRESS);
writeMemory(LED_ADDRESS, 1);
getch();
return 0;
}