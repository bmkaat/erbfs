#include<stdio.h>
#include<stdlib.h>
int main()
{
int i,j,k;
printf("number of rows: ");
scanf("%i", &i);
printf("number of columns: ");
scanf("%i", &j);
printf("number of elements: ");
scanf("%i", &k);
int game[i][j][k];
for (int i1=0; i1<i; i1++)
{
    for(int j1=0; j1<j; j1++)
    {   
        printf("enter elements of [%i][%i]", i1+1, j1+1);
        for (int k1=0; k1<k; k1++)
        {
            scanf("%d", &game[i1][j1][k1]);
        }
    }
}
/*for (int i1=0; i1<i; i1++)
{
    for(int j1=0; j1<j; j1++)
    {   
        printf("number of elements in [%i][%i]: ", i1+1,j1+1);
        scanf("%i", &k);
        int element[k];
        game[i1][j1]= element[k];
        printf("enter elements of [%i][%i]", i1+1,j1+1);
        for (int k1=0; k1<k; k1++)
        {
            int k2;
            scanf("%i", &k2);
            element[k1]=k2;
        }
    }
}

for (int i1=0; i1<i; i1++)
{
    printf("(");
    for(int j1=0; j1<j; j1++)
    {
        printf("[");
        for(int k1=0; k1<k; k1++)
        {
            printf("%d ", game[i1][j1][k1]);
        }
        printf("] ");
    }
    printf(")\n");
}
*/

printf("%d", game[1][0][1]);
    return 0;
}