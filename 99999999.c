#include<stdio.h>
#include<dos.h>
#include<conio.h>
void ISR()
{
printf("\n** Interrupt Received **\n");
printf("Executing Interrupt Service Routine...\n");
printf("I/O Operation completed.\n");
printf("Returning to Main Program...\n\n");
}
int main()
{
int i;
printf("\n Interrupt Driven I/O simulation\n\n");
for (i = 1; i <= 10; i++)
{
printf("CPU executing tasks %d\n", i);
sleep(1);
if (i == 5)
{
ISR();
}
}
printf("All CPU tasks completed.\n");
getch();
return 0;
}
