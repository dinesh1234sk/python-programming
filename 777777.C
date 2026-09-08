#include <stdio.h>

int main()
{

    char *instr[] = {
	"ADD R1,R2,R3",
	"SUB R4,R5,R6",
	"MUL R7,R8,R9"
    };

    char *stage[] = {"IF", "ID", "EX", "MEM", "WB"};

    int cycle, i, s;
    clrscr();
    printf("Instructions:\n");
    for(i=0;i<3;i++)
    printf("I%d:%s\n",i+1,instr[i]);
    printf("\nPipeline Execution\n");
    printf("Clock Cycle\tI1\tI2\tI3\n");

    for (cycle = 1; cycle <= 7; cycle++)
    {
	printf("%d\t\t", cycle);

	for (i = 0; i < 3; i++)
	{
	    s = cycle - i;

	    if (s > 0 && s <= 5)
		printf("%s\t", stage[s - 1]);
	    else
		printf(" \t");
	}

	printf("\n");
    }
    getch();
    return 0;
}
