#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    int i,j,k;
    printf("number of rows: ");
    scanf("%i", &i);
    printf("number of columns: ");
    scanf("%i", &j);
    k=j;
    int game[i][j][k];
    memset(game, 0, sizeof game);
    for (int i1=0; i1<i; i1++)
    {
        for(int j1=0; j1<j; j1++)
        {   
            printf("number of elements in [%i][%i]: ", i1+1, j1+1);
            int k1;
            scanf("%i", &k1);
            for (int k2=0; k2<k1; k2++)
            {
                printf("enter elements: ");
                int k3;
                scanf("%d", &k3);
                k3--;
                game[i1][j1][k3]=1;
            }
        }
    }
    int g,r;
    printf("how many green hints? ");
    scanf("%i", &g);
    int gh[i][g][k];
    printf("how many red hints? ");
    scanf("%i", &r);
    int rh[i][2*r][k];
    for(int g1=0; g1<g; g1++)
    {
        int g21,g22,e21,e22;
        printf("first row? ");
        scanf("%i", &g21);
        printf("element in first row? ");
        scanf("%i", &e21);
        printf("second row? ");
        scanf("%i", &g22);
        printf("element in second row? ");
        scanf("%i", &e22);
        gh[g21][g1][e21]=1;
        gh[g22][g1][e22]=1;
    }
    for(int r1=0; r1<(2*r): r1++)
    {
        int r21,r22,e21,e22;
        printf("first row? ");
        scanf("%i", &r21);
        printf("element in first row? ");
        scanf("%i", &e21);
        printf("second row? ");
        scanf("%i", &r22);
        printf("element in second row? ");
        scanf("%i", &e22);
        rh[r21][r1][e21]=1;
        rh[r22][r1][e22]=-1;
        r1++
        rh[r21][r1][e21]=-1;
        rh[r22][r1][e22]=1;
    }

    /*
    for (int i1=0; i1<i; i1++)
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
                printf("%d", game[i1][j1][k1]);
            }
            printf("]");
        }
        printf(")\n");
    }
    */
    return 0;
}