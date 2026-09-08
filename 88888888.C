#include <stdio.h>
#include <string.h>
#include<conio.h>
typedef struct
{
char opcode[10];
char dest[5];
char src1[5];
char src2[5];
} Instruction;
int main()
{
Instruction inst[] =
{
{"LW",  "R1", "R2", ""},
{"ADD", "R3", "R1", "R4"},
{"SUB", "R5", "R3", "R6"},
{"MUL", "R7", "R5", "R8"}
};
int i;
int n = 4;
int stalls = 0, forwards = 0;
printf("\nInstruction Sequence:\n");
for (i = 0; i < n; i++)
{
printf("%-5s %-5s %-5s %-5s\n",
inst[i].opcode,
inst[i].dest,
inst[i].src1,
inst[i].src2);
}
printf("\nHazard Detection and Resolution\n");
printf("--------------------------------\n");
for (i = 1; i < n; i++)
{
if (strcmp(inst[i - 1].dest, inst[i].src1) == 0 ||
strcmp(inst[i - 1].dest, inst[i].src2) == 0)
{
printf("\nHazard between I%d and I%d on register %s\n",
i, i + 1, inst[i].src1);
if (strcmp(inst[i - 1].opcode, "LW") == 0)
{
printf("Resolution: STALL inserted (Load-use hazard)\n");
stalls++;
}
else
{
printf("Resolution: FORWARDING applied\n");
forwards++;
}
}
}
printf("\n--------------------\n");
printf("Total forwardings: %d\n", forwards);
printf("Total stalls: %d\n", stalls);
getch();
return 0;
}