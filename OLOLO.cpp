#include<bits/stdc++.h>

using namespace std;

int main()
{

    int N,a=0,ans = 0;

    scanf("%d",&N);
    scanf("%d",&ans);

    for(int i=0;i<N-1;i++)
    {
        scanf("%d",&a);
        ans = ans^a;
    }

    printf("%d",ans);

    return 0;
}
