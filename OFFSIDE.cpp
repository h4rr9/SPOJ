#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    int A,D;
    while(1)
    {
        scanf("%d %d",&A,&D);

        if(A==0 && D==0)
           break;

        int A_dist[A],D_dist[D];

        for(int i=0;i<A;i++)
            scanf("%d",&A_dist[i]);
        for(int i=0;i<D;i++)
            scanf("%d",&D_dist[i]);

        sort(A_dist,A_dist+A);
        sort(D_dist,D_dist+D);

        if(A_dist[0]<D_dist[1])
            printf("Y\n");
        else
            printf("N\n");
    }
    return 0;
}
